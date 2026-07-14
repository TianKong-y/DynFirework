"""DynFirework 主窗口 支持 CB/DF 双后端切换."""
from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any

from dyn.env import RESOURCE_DIR, get_flag
from dyn.logging_config import setup_logging, get_logger

log = get_logger(__name__)

from PySide6.QtCore import QItemSelectionModel, Qt, Slot, QSettings
from PySide6.QtGui import QColor, QFont, QFontDatabase
from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtWidgets import (
	QApplication, QMainWindow, QTreeView, QFileDialog, QMessageBox,
	QMenu, QLabel, QDialog,
)

from dyn.lib.units import MinecraftPosition
from dyn.models.project import Backend
from dyn.models import Project

from dyn.models.df.base import Element as DfElement, ElementCategory
from dyn.models.df.composites import CompositeElement
from dyn.models.cb.base import Element as CbElement, ElementType as CbElementType
from dyn.models.cb.composites import TrajFireworkElement as CbTrajFireworkElement

from dyn.service.audio_service import load_waveform
from dyn.service.element_controller import (
	ElementController, DF_CATEGORY_DISPLAY, CB_CATEGORY_DISPLAY,
)
from dyn.service.export_service import ExportService
from dyn.service.metronome import Metronome
from dyn.service.playback_controller import PlaybackController
from dyn.service.project_manager import ProjectManager
from dyn.service.undo_manager import UndoManager

from dyn.components.element_browser import (
	ElementBrowserModel, CbElementBrowserModel,
	ProxyNode,
)
from dyn.components.inspector import Inspector
from dyn.components.property_panel import PropertyPanel, CbPropertyPanel
from dyn.components.df.timeline import DFTimelineWidget
from dyn.components.df.timeline.theme import TICKS_PER_SECOND
from dyn.components.cb.timeline import ParticleexTimelineWidget
from dyn.components.transport_bar import TransportBar
from dyn.components.pos_select.select_center import PosSelectMainWindow

from dyn.actions.about import DYNAboutWindow
from dyn.actions.help import DYNHelpWindow
from dyn.actions.new_project import NewProjectDialog
from dyn.actions.project_settings import ProjectSettingsDialog
from dyn.actions.export_datapack import ExportDatapackDialog

_DF_CATEGORY_ICONS: dict[ElementCategory, str] = {
	ElementCategory.FIREWORK: "*",
	ElementCategory.TRAJECTORY: "/",
	ElementCategory.EFFECT: "-",
	ElementCategory.COMPOSITE: "+",
}

_CB_CATEGORY_ICONS: dict[CbElementType, str] = {
	CbElementType.TRAJECTORY: "/",
	CbElementType.FIREWORK: "*",
	CbElementType.TRAJ_FIREWORK: "+",
}

def _elem_info(elem) -> str:
	"""返回元素的关键信息字符串，兼容 cb/df."""
	if elem is None:
		return "None"
	if isinstance(elem, DfElement):
		return f"{elem.name} cat={elem.category.value} t={elem.start_time:.2f}s dur={elem.duration:.2f}s"
	elif isinstance(elem, CbElement):
		info = f"{elem.name} type={elem.element_type.name} t={elem.start_tick}t"
		if isinstance(elem, CbTrajFireworkElement):
			info += f" traj={elem.traj_duration_ticks}t fw={elem.fw_duration_ticks}t"
		else:
			info += f" dur={elem.duration_ticks}t"
		return info
	return f"{elem.name}"

class MainWin(QMainWindow):
	"""DynFirework 主窗口 支持 CB/DF 双后端切换."""

	def __init__(self) -> None:
		super().__init__()
		log.debug("MainWin 初始化开始")
		self.setWindowTitle("DynFirework   Minecraft 烟花设计工具")
		self.resize(1600, 900)

		# Backend state
		self._backend: Backend | None = None
		self._controller: ElementController | None = None

		# 测试模式
		self._test_mode = get_flag("DYN_TEST_ENABLED")

		# 共享服务
		self._project_manager = ProjectManager(self)
		self._export_service = ExportService(self)
		self._playback = PlaybackController(self)
		self._metronome = Metronome(self) if self._test_mode else None
		self._pos_selector = PosSelectMainWindow()

		# 共享 UI
		self._inspector = Inspector()
		self._transport_bar = None  # 在 _inject_components() 中创建
		self._help_window = DYNHelpWindow()

		# 后端特定 UI (在 _activate_backend 中创建)
		self._ui: Any = None
		self._timeline: Any = None
		self._property_panel: Any = None
		self._element_browser_model: Any = None
		self._tree_view: QTreeView | None = None

		self._syncing_tree: bool = False
		self._pending_position_target: str = ""

		# 构建初始 UI
		self._connect_shared_signals()
		self._restore_window_state()

		# 激活默认后端
		self._activate_backend(Backend.DF)
		proj = self._project_manager.project
		self._ui.label.setText(f"{proj.name} - {proj.mc_version}")

	# Backend Switching

	def _activate_backend(self, backend: Backend) -> None:
		"""根据后端初始化/切换整个 UI 组件树."""
		if self._backend == backend and self._controller is not None:
			return
		if self._backend is not None:
			self._deactivate_current_backend()
		self._backend = backend

		if backend == Backend.CB:
			from dyn.ui.mainwin_cb import Ui_MainWindow as MWUI
		else:
			from dyn.ui.mainwin_df import Ui_MainWindow as MWUI
		self._ui = MWUI()
		self._ui.setupUi(self)

		self._controller = ElementController(backend=backend, parent=self)
		self._undo_manager = UndoManager(self._controller, self)

		if backend == Backend.CB:
			self._init_cb_ui()
		else:
			self._init_df_ui()

		self._inject_components()
		self._connect_menu_actions()
		self._connect_backend_signals()
		self._undo_manager.clear()
		self._inspector.clear()

	def _deactivate_current_backend(self) -> None:
		"""清理当前后端的所有信号和组件."""
		if self._controller:
			try:
				self._controller.element_added.disconnect()
				self._controller.element_removed.disconnect()
				self._controller.element_changed.disconnect()
				self._controller.selection_changed.disconnect()
			except (RuntimeError, TypeError):
				pass
		for slot in (self._on_playback_position_cb, self._on_playback_position_df):
			try:
				self._playback.position_changed.disconnect(slot)
			except (RuntimeError, TypeError):
				pass
		try:
			self._playback.state_changed.disconnect(self._on_playback_state_for_actions)
		except (RuntimeError, TypeError):
			pass
		if self._metronome is not None:
			try:
				self._playback.position_changed.disconnect(self._metronome.on_tick)
				self._playback.state_changed.disconnect(self._on_metronome_state_changed)
			except (RuntimeError, TypeError):
				pass
		if self._timeline:
			try:
				self._timeline.playback_cursor_changed.disconnect()
			except (RuntimeError, TypeError):
				pass
		if self._transport_bar:
			try:
				self._transport_bar.beat_lines_toggled.disconnect()
			except (RuntimeError, TypeError):
				pass
			try:
				self._transport_bar.time_marks_toggled.disconnect()
			except (RuntimeError, TypeError):
				pass
			try:
				self._transport_bar.metronome_toggled.disconnect()
			except (RuntimeError, TypeError):
				pass
		self._timeline = None
		self._property_panel = None
		self._element_browser_model = None
		self._tree_view = None
		self._transport_bar = None
		self._ui = None

	def _init_cb_ui(self) -> None:
		"""初始化 ColorBlock 后端 UI 组件."""
		log.debug("初始化 CB UI 组件")
		self._element_browser_model = CbElementBrowserModel()
		self._element_browser_model.set_controller(self._controller)
		log.debug("CB 元素浏览器模型已创建")

		self._timeline = ParticleexTimelineWidget()
		self._timeline.set_controller(self._controller)
		log.debug("CB 时间线已创建")

		self._property_panel = CbPropertyPanel(self._controller)
		log.debug("CB 属性面板已创建")

	def _init_df_ui(self) -> None:
		"""初始化 DynFirework 后端 UI 组件."""
		log.debug("初始化 DF UI 组件")
		self._element_browser_model = ElementBrowserModel()
		self._element_browser_model.set_controller(self._controller)
		log.debug("DF 元素浏览器模型已创建")

		self._timeline = DFTimelineWidget()
		self._timeline.set_controller(self._controller)
		log.debug("DF 时间线已创建")

		self._property_panel = PropertyPanel(self._controller)
		log.debug("DF 属性面板已创建")

	# Component Injection

	def _inject_components(self) -> None:
		"""将代码创建的组件注入到 Designer 预设的占位控件中."""
		ui = self._ui

		# 元素列表
		self._tree_view = ui.element_list_tree_view
		f = QFont()
		f.setFamilies(["Ark Pixel 12px P zh_cn"])
		self._tree_view.setFont(f)
		self._tree_view.setModel(self._element_browser_model)
		self._tree_view.setHeaderHidden(False)
		self._tree_view.setAnimated(True)
		self._tree_view.setExpandsOnDoubleClick(False)
		self._tree_view.expandAll()
		self._tree_view.setContextMenuPolicy(Qt.CustomContextMenu)
		self._tree_view.customContextMenuRequested.connect(self._on_tree_context_menu)

		# 属性面板 - 设入 QScrollArea
		ui.property_panel_area.setWidget(self._property_panel)

		# 检查器 - 替换 inspector 占位
		ui.verticalLayout_3.replaceWidget(ui.inspector, self._inspector)
		ui.inspector.hide()
		ui.inspector.deleteLater()

		# 传输栏 - 创建控制器，绑定 .ui 预设控件
		self._transport_bar = TransportBar(
			self._playback,
			btn_play=ui.timeline_play_pause,
			btn_stop=ui.timeline_stop,
			btn_replay=ui.timeline_replay,
			btn_hint_tick=ui.timeline_toggle_hint_tick,
			btn_time_tick=ui.timeline_toggle_time_tick,
			label_time=ui.timeline_time,
			label_tick=ui.timeline_tick,
			slider_volume=ui.timeline_volume_adjust,
			label_music=ui.timeline_music_name,
			label_bpm=ui.timeline_bpm,
			btn_metronome=ui.timeline_metronome_toggle if self._test_mode else None,
		)

		# 时间线 - 设入 timeline_area
		ui.timeline_area.setWidget(self._timeline)

		# 面板可见性引用
		self._left_panel = ui.element_list_frame
		self._right_panel = ui.inspector_frame
		self._bottom_panel = ui.lower_frame

		# 状态栏
		self._status_label = QLabel("就绪")
		ui.statusbar.addWidget(self._status_label)

	# Menu Actions

	def _connect_menu_actions(self) -> None:
		"""绑定 Designer 预定义的 QAction 到槽函数."""
		ui = self._ui

		# 文件
		ui.new_proj_action.triggered.connect(self._on_new_project)
		ui.open_proj_action.triggered.connect(self._on_open_project)
		ui.save_action.triggered.connect(self._on_save_project)
		ui.save_as_action.triggered.connect(self._on_save_as_project)
		ui.import_music_action.triggered.connect(self._on_import_music)
		ui.import_point_action.triggered.connect(self._pos_selector.import_data)
		ui.export_datapack_action.triggered.connect(self._on_export_datapack)
		ui.export_point_action.triggered.connect(self._pos_selector.export_data)

		# 编辑 - 新建元素 (按后端)
		self._connect_new_element_actions()
		ui.undo_action.triggered.connect(self._undo_manager.undo)
		ui.redo_action.triggered.connect(self._undo_manager.redo)
		self._undo_manager.can_undo_changed.connect(ui.undo_action.setEnabled)
		self._undo_manager.can_redo_changed.connect(ui.redo_action.setEnabled)
		self._undo_manager.undo_text_changed.connect(
			lambda t: ui.undo_action.setText(f"撤销 {t}" if t else "撤销"))
		self._undo_manager.redo_text_changed.connect(
			lambda t: ui.redo_action.setText(f"重做 {t}" if t else "重做"))
		ui.copy_element_action.triggered.connect(self._on_clone_element)
		ui.delete_element_action.triggered.connect(self._on_delete_selected)
		ui.play_action.triggered.connect(self._playback.play)
		ui.pause_action.triggered.connect(self._playback.pause)
		ui.stop_action.triggered.connect(self._playback.stop)
		ui.backward_action.triggered.connect(lambda: self._playback.seek_to_tick(0))
		self._playback.state_changed.connect(self._on_playback_state_for_actions)
		# 刻度线菜单 <-> 传输栏按钮 双向同步
		ui.hint_tick_toggle_action.toggled.connect(
			ui.timeline_toggle_hint_tick.setChecked)
		ui.time_tick_toggle_action.toggled.connect(
			ui.timeline_toggle_time_tick.setChecked)

		# 视图
		ui.pos_selector_action.triggered.connect(self._pos_selector.showNormal)
		self._setup_test_features()
		# 面板可见性 action 已在 .ui 中预连接到对应 frame

		# 项目
		ui.proj_settings_action.triggered.connect(self._on_project_settings)

		# 关于
		ui.about_DynFirework_action.triggered.connect(
			lambda: DYNAboutWindow().exec())
		ui.help_action.triggered.connect(
			self._help_window.show)

	def _connect_new_element_actions(self) -> None:
		"""根据后端连接新建元素的菜单 action."""
		ui = self._ui
		if self._backend == Backend.CB:
			ui.new_firework_action.triggered.connect(
				lambda: self._on_new_element(CbElementType.FIREWORK))
			ui.new_traj_action.triggered.connect(
				lambda: self._on_new_element(CbElementType.TRAJECTORY))
			ui.new_tf_action.triggered.connect(
				lambda: self._on_new_element(CbElementType.TRAJ_FIREWORK))
		else:
			ui.new_explosion_action.triggered.connect(
				lambda: self._on_new_element(ElementCategory.FIREWORK))
			ui.new_traj_action.triggered.connect(
				lambda: self._on_new_element(ElementCategory.TRAJECTORY))
			ui.new_effect_action.triggered.connect(
				lambda: self._on_new_element(ElementCategory.EFFECT))
			ui.new_complex_elem_action.triggered.connect(
				lambda: self._on_new_element(ElementCategory.COMPOSITE))

	def _update_media_actions(self) -> None:
		"""根据媒体加载状态和播放状态更新播放相关 action."""
		ui = self._ui
		has_media = self._playback.player.mediaStatus() != QMediaPlayer.MediaStatus.NoMedia
		state = self._playback.player.playbackState()
		is_playing = state == QMediaPlayer.PlaybackState.PlayingState
		ui.play_action.setEnabled(has_media and not is_playing)
		ui.pause_action.setEnabled(has_media and is_playing)
		ui.stop_action.setEnabled(has_media and state != QMediaPlayer.PlaybackState.StoppedState)
		ui.backward_action.setEnabled(has_media)

	def _on_playback_state_for_actions(self, state: str) -> None:
		"""播放状态改变时更新菜单 action 的启用状态."""
		self._update_media_actions()

	def _set_metronome_enabled(self, enabled: bool) -> None:
		"""同步菜单 action、传输栏按钮和 Metronome 的启用状态."""
		if self._metronome is None:
			return
		self._metronome.enabled = enabled
		if self._ui is not None:
			self._ui.metronome_action_toggle.setChecked(enabled)
			self._ui.timeline_metronome_toggle.setChecked(enabled)

	def _on_metronome_state_changed(self, state: str) -> None:
		if self._metronome is not None:
			self._metronome.notify_state(state)

	def _sync_metronome_settings(self) -> None:
		"""从当前项目同步节拍器参数."""
		if self._metronome is None:
			return
		proj = self._project_manager.project
		self._metronome.set_bpm(proj.bpm)
		self._metronome.set_time_signature(proj.time_signature)
		self._metronome.set_audio_offset_ms(proj.audio_offset_ms)

	def _setup_test_features(self) -> None:
		"""集中管理测试功能：根据 _test_mode 切换 enable/disable 状态."""
		ui = self._ui
		test_actions = [
			ui.metronome_action_toggle,
			ui.palette_action,
			ui.pos_selector_3d_action,
		]
		for action in test_actions:
			action.setEnabled(self._test_mode)
		ui.timeline_metronome_toggle.setEnabled(self._test_mode)
		if self._test_mode:
			try:
				ui.metronome_action_toggle.toggled.disconnect(self._set_metronome_enabled)
			except (RuntimeError, TypeError):
				pass
			ui.metronome_action_toggle.toggled.connect(self._set_metronome_enabled)

	# Shared Signals

	def _connect_shared_signals(self) -> None:
		log.debug("连接共享信号")
		self._export_service.export_finished.connect(self._on_export_finished)
		self._export_service.export_progress.connect(
			lambda p: self.statusBar().showMessage(f"导出中... {p}%")
		)
		self._project_manager.project_opened.connect(self._on_project_opened)
		self._pos_selector.send_chosen_point.connect(self._on_position_chosen)

	def _connect_backend_signals(self) -> None:
		"""连接后端特定的信号 (切换后端后重新连接)."""
		log.debug(f"连接 {self._backend} 后端信号")
		ct = self._controller

		# 通用 Controller 信号
		ct.selection_changed.connect(self._on_controller_selection)
		ct.element_added.connect(self._on_element_count_changed)
		ct.element_removed.connect(self._on_element_count_changed)

		# 属性面板信号
		self._property_panel.property_changed.connect(self._on_property_changed)
		self._property_panel.element_name_changed.connect(
			lambda eid, name: ct.set_property(eid, "name", name)
		)
		self._property_panel.position_select_requested.connect(
			self._on_position_select_requested
		)

		# 元素浏览器 -> Controller 选中同步
		self._element_browser_model.selection_changed.connect(ct.select_element)

		# Tree view selection
		self._tree_view.selectionModel().selectionChanged.connect(
			self._on_tree_selection_changed
		)

		# 时间线信号 (按后端连接不同的 handler)
		self._timeline.delete_requested.connect(self._on_delete_selected)
		if self._backend == Backend.CB:
			self._connect_cb_timeline_signals()
		else:
			self._connect_df_timeline_signals()

		# 播放控制 signal
		if self._backend == Backend.CB:
			self._playback.position_changed.connect(self._on_playback_position_cb)
			self._timeline.playback_cursor_changed.connect(self._on_timeline_cursor_cb)
		else:
			self._playback.position_changed.connect(self._on_playback_position_df)
			self._timeline.playback_cursor_changed.connect(self._on_timeline_cursor_df)

		# TransportBar 在 _inject_components 创建时已自连接 position_changed/state_changed
		# 辅助线/刻度线切换 (每次切换后端需重连)
		self._transport_bar.beat_lines_toggled.connect(self._timeline.set_show_beat_lines)
		self._transport_bar.time_marks_toggled.connect(self._timeline.set_show_time_marks)
		if self._metronome is not None:
			self._transport_bar.metronome_toggled.connect(self._set_metronome_enabled)
			self._playback.position_changed.connect(self._metronome.on_tick)
			self._playback.state_changed.connect(self._on_metronome_state_changed)
			self._sync_metronome_settings()

	def _connect_cb_timeline_signals(self) -> None:
		tracks = [self._timeline.fw_track, self._timeline.traj_track]
		for track in tracks:
			track.element_selected.connect(self._on_timeline_select)
			track.element_moved.connect(self._on_timeline_element_moved_cb)
			track.element_resized.connect(self._on_timeline_element_resized_cb)
			track.drag_undo_begin.connect(lambda: self._undo_manager.begin_macro("拖拽修改"))
			track.drag_undo_end.connect(self._undo_manager.end_macro)

	def _connect_df_timeline_signals(self) -> None:
		tracks = [
			self._timeline.fw_track, self._timeline.traj_track,
			self._timeline.effect_track, self._timeline.composite_track,
		]
		for track in tracks:
			track.element_selected.connect(self._on_timeline_select)
			track.element_moved.connect(self._on_timeline_element_moved_df)
			track.element_resized.connect(self._on_timeline_element_resized_df)
			track.drag_undo_begin.connect(lambda: self._undo_manager.begin_macro("拖拽修改"))
			track.drag_undo_end.connect(self._undo_manager.end_macro)

	# 文件操作

	def _on_new_project(self) -> None:
		log.debug("新建项目")
		if self._project_manager.is_modified:
			reply = QMessageBox.question(
				self, "新建项目", "当前项目未保存，是否继续？",
				QMessageBox.Yes | QMessageBox.No,
			)
			if reply == QMessageBox.No:
				return

		dlg = NewProjectDialog(self)
		if dlg.exec() != QDialog.DialogCode.Accepted:
			return

		proj = self._project_manager.new_project(
			name=dlg.project_name,
			backend=dlg.backend,
			mc_version=dlg.mc_version,
			bpm=dlg.bpm,
			time_signature=dlg.time_signature,
			audio_offset_ms=dlg.audio_offset_ms,
		)
		self._activate_backend(proj.backend)
		self._controller.load_from_project(proj)
		self._element_browser_model.load_elements(self._controller.all_elements)
		self._timeline.on_elements_changed()
		self._inspector.clear()
		self._playback.stop()
		self._transport_bar.set_bpm(proj.bpm)
		self._timeline.update_music_info(proj.bpm, proj.audio_offset_ms, proj.time_signature, proj.ticks_per_beat)
		self._sync_metronome_settings()
		log.debug(f"新建项目: name={proj.name}, backend={proj.backend.value}, bpm={proj.bpm}, mc={proj.mc_version}")
		self._ui.label.setText(f"{proj.name} - {proj.mc_version}")
		self.setWindowTitle(f"DynFirework   {proj.name}")
		self.statusBar().showMessage(f"已创建: {proj.name} | BPM: {proj.bpm:.0f} | MC {proj.mc_version}")

	def _on_open_project(self) -> None:
		if self._project_manager.is_modified:
			reply = QMessageBox.question(
				self, "打开项目", "当前项目未保存，是否继续？",
				QMessageBox.Yes | QMessageBox.No,
			)
			if reply == QMessageBox.No:
				return

		path, _ = QFileDialog.getOpenFileName(
			self, "打开项目", "", "DynFirework 项目 (*.dyn);;所有文件 (*.*)"
		)
		if not path:
			log.debug("用户取消打开项目")
			return
		try:
			log.debug(f"打开项目: {path}")
			proj = self._project_manager.open_project(path)
			self._activate_backend(proj.backend)
			self._inspector.clear()
			self._playback.stop()
			self._controller.load_from_project(proj)
			self._element_browser_model.load_elements(self._controller.all_elements)
			self._pos_selector_load_saved(proj)
			if proj.has_music:
				music_path = self._project_manager.get_music_temp_path()
				if music_path:
					self._playback.load_music(music_path)
					self._playback.set_bpm(proj.bpm)
					self._load_waveform(music_path)
					self._transport_bar.set_music_path(proj.music_original_name)
					self._update_media_actions()
			self._timeline.on_elements_changed()
			self._tree_view.expandAll()
			self._transport_bar.set_bpm(proj.bpm)
			self._timeline.update_music_info(proj.bpm, proj.audio_offset_ms, proj.time_signature, proj.ticks_per_beat)
			self._sync_metronome_settings()
			self._ui.label.setText(f"{proj.name} - {proj.mc_version}")
			self.setWindowTitle(f"DynFirework   {proj.name}")
			self.statusBar().showMessage(f"已打开: {path}")
		except Exception as e:
			log.error(f"打开项目失败: {e}", exc_info=True)
			QMessageBox.critical(self, "打开失败", str(e))

	def _sync_positions_to_project(self) -> None:
		pts = self._pos_selector.points
		self._project_manager.project.saved_positions = [
			{"x": p.x, "y": p.y, "z": p.z, "label": p.label,
			 "color": {"r": p.pix_color.red(), "g": p.pix_color.green(), "b": p.pix_color.blue()}}
			for p in pts
		]

	def _pos_selector_load_saved(self, proj: Project) -> None:
		"""从项目加载保存的位置点到位置选择器."""
		try:
			saved = proj.saved_positions
			if saved:
				pts = []
				for p in saved:
					c = p.get("color", {})
					pts.append(MinecraftPosition(
						x=float(p["x"]), y=float(p["y"]), z=float(p["z"]),
						label=str(p.get("label", "")),
						main_color=QColor(c.get("r", 255), c.get("g", 255), c.get("b", 255)),
					))
				self._pos_selector.points.clear()
				self._pos_selector.points.extend(pts)
				self._pos_selector.fastsearch.clear()
				self._pos_selector.fastsearch.update((int(pt.x), int(pt.z)) for pt in pts)
				self._pos_selector.pix_element_list.get_element_list(self._pos_selector.points)
		except Exception as e:
			log.warning(f"恢复位置点失败: {e}")

	def _on_save_project(self) -> None:
		self._controller.to_project(self._project_manager.project)
		self._sync_positions_to_project()
		if not self._project_manager.has_file:
			log.debug("无文件路径, 转入另存为")
			self._on_save_as_project()
			return
		log.debug(f"保存项目: {self._project_manager.file_path}")
		if self._project_manager.save_project():
			self.statusBar().showMessage(f"已保存: {self._project_manager.file_path}")
		else:
			log.error("保存项目失败")
			QMessageBox.warning(self, "保存失败", "无法保存项目。")

	def _on_save_as_project(self) -> None:
		path, _ = QFileDialog.getSaveFileName(
			self, "另存为", "untitled.dyn", "DynFirework 项目 (*.dyn)"
		)
		if not path:
			log.debug("用户取消另存为")
			return
		log.debug(f"另存为: {path}")
		self._controller.to_project(self._project_manager.project)
		self._sync_positions_to_project()
		if self._project_manager.save_project(path):
			self.statusBar().showMessage(f"已保存: {path}")
		else:
			log.error("另存为失败")
			QMessageBox.warning(self, "保存失败", "无法保存项目。")

	def _on_import_music(self) -> None:
		path, _ = QFileDialog.getOpenFileName(
			self, "导入音乐", "",
			"音频文件 (*.mp3 *.wav *.ogg *.flac);;所有文件 (*.*)"
		)
		if not path:
			return
		log.debug(f"导入音乐: {path}")
		if not self._project_manager.set_music(path):
			QMessageBox.warning(self, "导入失败", "无法读取音乐文件。")
			return
		self._playback.load_music(path)
		self._load_waveform(path)
		self._transport_bar.set_music_path(Path(path).name)
		self._update_media_actions()
		self.statusBar().showMessage(f"已导入: {Path(path).name}")

	def _load_waveform(self, path: str) -> None:
		samples, sr = load_waveform(path)
		if samples:
			bpm = self._project_manager.project.bpm
			self._timeline.set_waveform_data(samples, sr, bpm)

	def _on_export_datapack(self) -> None:
		elements = self._controller.all_elements
		log.debug(f"导出数据包: {len(elements)} 个元素")
		if not elements:
			QMessageBox.warning(self, "无元素", "请先创建至少一个元素。")
			log.warning("导出取消: 无元素可导出")
			return

		proj = self._project_manager.project
		dlg = ExportDatapackDialog(proj.name, proj.mc_version, self)
		if dlg.exec() != QDialog.DialogCode.Accepted:
			return

		ns = dlg.namespace or "fireworks1"
		if not re.match(r'^[a-z0-9_\.]+$', ns):
			QMessageBox.warning(self, "无效命名空间", "命名空间仅限小写字母、数字、下划线和点。")
			log.warning(f"无效命名空间: {ns}")
			return

		output_dir = QFileDialog.getExistingDirectory(self, "选择输出目录")
		if not output_dir:
			return

		log.debug(f"导出数据包: namespace={ns}, backend={proj.backend.value}")
		self._export_service.export_to_datapack(
			elements, output_dir, ns,
			backend=proj.backend,
			datapack_name=dlg.pack_name, description=dlg.description,
			pack_format=dlg.pack_format, mc_version=proj.mc_version,
		)

	def _on_export_finished(self, success: bool, message: str) -> None:
		if success:
			log.debug(f"导出成功: {message}")
			QMessageBox.information(self, "导出完成", message)
		else:
			log.error(f"导出失败: {message}")
			QMessageBox.critical(self, "导出失败", message)

	# 编辑操作

	def _on_new_element(self, category) -> None:
		"""创建元素 按 backend 获取光标时间和类别标签."""
		if self._backend == Backend.CB:
			cursor = self._timeline.playback_tick
			display = CB_CATEGORY_DISPLAY
		else:
			cursor = self._timeline.playback_time
			display = DF_CATEGORY_DISPLAY

		cat_label = display.get(category, category.value)
		count = len(self._controller.get_elements_by_category(category))
		elem = self._controller.create_element(
			category=category,
			name=f"{cat_label} {count}",
			start_time=round(cursor, 2) if self._backend != Backend.CB else cursor,
		)
		log.debug(f"创建元素: {_elem_info(elem)}")
		self._undo_manager.push_add_element(elem)
		self._tree_view.expandAll()
		self._controller.select_element(elem.id)
		self.statusBar().showMessage(f"已创建: {elem.name}")

	def _on_clone_element(self) -> None:
		eid = self._controller.selected_id
		if not eid:
			return
		cloned = self._controller.clone_element(eid)
		if cloned:
			log.debug(f"复制元素: src={eid} -> new={cloned.id}, name={cloned.name}")
			self._undo_manager.push_add_element(cloned)
			self._tree_view.expandAll()
			self.statusBar().showMessage(f"已复制: {cloned.name}")

	def _on_delete_selected(self) -> None:
		eid = self._controller.selected_id
		if not eid:
			log.debug("删除取消: 无选中元素")
			return
		elem = self._controller.get_element(eid)
		log.debug(f"删除元素: {_elem_info(elem)}")
		if elem:
			self._undo_manager.push_remove_element(elem)
		self._tree_view.expandAll()
		self.statusBar().showMessage("已删除")

	# 选中同步

	def _on_tree_selection_changed(self, selected, deselected) -> None:
		if self._syncing_tree or not selected.indexes():
			return
		idx = selected.indexes()[0]
		node = idx.internalPointer()

		# ProxyNode: 复合/组合元素的子代理节点
		if isinstance(node, ProxyNode):
			if self._backend == Backend.CB:
				self._on_tree_proxy_selected_cb(node)
			else:
				self._on_tree_proxy_selected_df(node)
			return

		# 普通元素节点
		elem = self._element_browser_model.get_element_from_index(idx)
		if elem is not None:
			self._controller.select_element(elem.id)
			self._property_panel.load_element(elem, "")
			if self._backend == Backend.CB and isinstance(elem, CbTrajFireworkElement):
				self._timeline.fw_track.set_selection(elem.id + "::fw")
				self._timeline.traj_track.set_selection(elem.id)
			elif isinstance(elem, CompositeElement):
				for t in self._get_df_tracks():
					t.set_selection(elem.id)

	def _on_tree_proxy_selected_cb(self, node: ProxyNode) -> None:
		"""CB 后端: TF 代理节点选中处理."""
		part = node.data
		parent_node = node.parent
		parent_elem = parent_node.data
		self._controller._selected_id = parent_elem.id
		self._controller.selection_changed.emit(parent_elem.id)
		part_id = "traj" if part == "_tf_traj" else "fw"
		self._timeline._selected_id = parent_elem.id
		self._timeline.fw_track.set_selection("")
		self._timeline.traj_track.set_selection("")
		if part == "_tf_traj":
			self._timeline.traj_track.set_selection(parent_elem.id)
		else:
			self._timeline.fw_track.set_selection(parent_elem.id + "::fw")
		self._property_panel.load_element(parent_elem, part_id)

	def _on_tree_proxy_selected_df(self, node: ProxyNode) -> None:
		"""DF 后端: 复合代理节点选中处理."""
		part = node.data
		parent_node = node.parent
		parent_elem = parent_node.data
		self._controller._selected_id = parent_elem.id
		self._controller.selection_changed.emit(parent_elem.id)

		part_map = {
			"_comp_primary": "primary",
			"_comp_secondary": "secondary",
			"_comp_clustered": "clustered",
			"_comp_expanding": "expanding",
			"_tf_traj": "traj",
			"_tf_fw": "fw",
		}
		part_id = part_map.get(part, part)

		proxy_id: str = parent_elem.id
		if part_id != "traj":
			proxy_id = f"{parent_elem.id}::{part_id}"

		self._timeline._selected_id = proxy_id
		for t in self._get_df_tracks():
			t.set_selection("")

		if part_id == "traj":
			self._timeline.traj_track.set_selection(parent_elem.id)
		else:
			self._timeline.fw_track.set_selection(proxy_id)

		self._property_panel.load_element(parent_elem, part_id)

	def _get_df_tracks(self) -> list:
		return [
			self._timeline.fw_track, self._timeline.traj_track,
			self._timeline.effect_track, self._timeline.composite_track,
		]

	@Slot(str)
	def _on_controller_selection(self, element_id: str) -> None:
		elem = self._controller.get_element(element_id)
		if elem:
			log.debug(f"控制器选中: {_elem_info(elem)}")
		else:
			log.debug(f"控制器选中: id={element_id} (未找到)")
		self._property_panel.load_element(elem)
		self._inspector.show_element(elem)

		self._syncing_tree = True
		try:
			sel = self._tree_view.selectionModel()
			model_idx = self._element_browser_model.get_index_for_element(element_id)
			if model_idx.isValid():
				sel.select(model_idx, QItemSelectionModel.SelectionFlag.ClearAndSelect | QItemSelectionModel.SelectionFlag.Rows)
			else:
				sel.clearSelection()
		finally:
			self._syncing_tree = False

		if elem:
			if self._backend == Backend.CB:
				self._status_label.setText(f"已选中: {elem.name} (tick={elem.start_tick})")
			else:
				self._status_label.setText(f"已选中: {elem.name} ({elem.start_time:.2f}s)")
			self._ui.inspector_target.setText(elem.name)
		else:
			self._status_label.setText("未选中")
			self._ui.inspector_target.setText("")

	def _on_element_count_changed(self, *args) -> None:
		count = len(self._controller.all_elements)
		has_elements = count > 0
		self._ui.copy_element_action.setEnabled(has_elements)
		self._ui.delete_element_action.setEnabled(has_elements)
		log.debug(f"元素数量变更: {count}")
		self.statusBar().showMessage(f"共 {count} 个元素", 3000)

	def _on_tree_context_menu(self, pos) -> None:
		menu = QMenu(self)
		idx = self._tree_view.indexAt(pos)
		elem = self._element_browser_model.get_element_from_index(idx) if idx.isValid() else None

		new_menu = menu.addMenu("新建元素")
		if self._backend == Backend.CB:
			cats = list(CbElementType)
			icons = _CB_CATEGORY_ICONS
			display = CB_CATEGORY_DISPLAY
		else:
			cats = list(ElementCategory)
			icons = _DF_CATEGORY_ICONS
			display = DF_CATEGORY_DISPLAY
		for cat in cats:
			icon = icons.get(cat, "")
			label = display.get(cat, cat.value)
			act = new_menu.addAction(f"{icon} {label}")
			act.triggered.connect(lambda checked, c=cat: self._on_new_element(c))

		if elem is not None:
			menu.addSeparator()
			act_clone = menu.addAction("复制元素")
			act_clone.triggered.connect(self._on_clone_element)
			act_del = menu.addAction("删除元素")
			act_del.triggered.connect(self._on_delete_selected)

		menu.exec(self._tree_view.viewport().mapToGlobal(pos))

	# 时间线拖拽 (CB: tick)

	def _on_timeline_select(self, element_id: str) -> None:
		"""时间线选中 代理元素只高亮自身，面板加载父元素."""
		log.debug(f"时间线选中: id={element_id}")
		if not element_id:
			self._controller.clear_selection()
			return
		real_id, part = ElementController.resolve_proxy_id(element_id)
		parent = self._controller.get_element(real_id)

		# 清除所有轨道选中
		if self._backend == Backend.CB:
			self._timeline.fw_track.set_selection(element_id)
			self._timeline.traj_track.set_selection(element_id)
		else:
			for t in self._get_df_tracks():
				t.set_selection(element_id)

		if part:
			self._timeline._selected_id = element_id
			if parent:
				self._property_panel.load_element(parent)
				self._inspector.show_element(parent)
				self._status_label.setText(f"已选中: {parent.name} ({_elem_info(parent)})")
			return
		self._controller.select_element(element_id)

	def _on_timeline_element_moved_cb(self, element_id: str, new_tick: int, old_tick: int) -> None:
		real_id, part = ElementController.resolve_proxy_id(element_id)
		elem = self._controller.get_element(real_id)
		log.debug(f"时间线移动(CB): {element_id} tick={new_tick} old={old_tick} real_id={real_id}")
		if elem:
			key = "start_tick"
			self._undo_manager.push_property_change(real_id, key, old_tick, new_tick)
			self._controller.element_changed.emit(real_id, "drag", None)
			self._property_panel.load_element(elem)
			self._inspector.refresh(elem)
			self._project_manager.mark_modified()

	def _on_timeline_element_resized_cb(self, element_id: str, new_dur: int, old_dur: int) -> None:
		real_id, part = ElementController.resolve_proxy_id(element_id)
		elem = self._controller.get_element(real_id)
		log.debug(f"时间线缩放(CB): {element_id} dur={new_dur} old={old_dur} real_id={real_id} part={part}")
		if elem:
			if isinstance(elem, CbTrajFireworkElement):
				if part == "traj":
					key = "traj_duration_ticks"
				else:
					key = "fw_duration_ticks"
			else:
				key = "duration_ticks"
			self._undo_manager.push_property_change(real_id, key, old_dur, new_dur)
			self._controller.element_changed.emit(real_id, "drag", None)
			self._property_panel.load_element(elem)
			self._inspector.refresh(elem)
			self._project_manager.mark_modified()

	# 时间线拖拽 (DF: second)

	def _on_timeline_element_moved_df(self, element_id: str, new_time: float, old_time: float) -> None:
		real_id, part = ElementController.resolve_proxy_id(element_id)
		elem = self._controller.get_element(real_id)
		log.debug(f"时间线移动(DF): {element_id} time={new_time:.2f}s old={old_time:.2f}s real_id={real_id}")
		if elem:
			key = "start_time"
			self._undo_manager.push_property_change(real_id, key, old_time, new_time)
			self._controller.element_changed.emit(real_id, "drag", None)
			self._property_panel.load_element(elem)
			self._inspector.refresh(elem)
			self._project_manager.mark_modified()

	def _on_timeline_element_resized_df(self, element_id: str, new_dur: float, old_dur: float) -> None:
		real_id, part = ElementController.resolve_proxy_id(element_id)
		elem = self._controller.get_element(real_id)
		log.debug(f"时间线缩放(DF): {element_id} dur={new_dur:.2f}s old={old_dur:.2f}s real_id={real_id} part={part}")
		if elem:
			key = "duration"
			self._undo_manager.push_property_change(real_id, key, old_dur, new_dur)
			self._controller.element_changed.emit(real_id, "drag", None)
			self._property_panel.load_element(elem)
			self._inspector.refresh(elem)
			self._project_manager.mark_modified()

	# 播放控制

	def _on_playback_position_cb(self, tick: int) -> None:
		self._timeline.set_playback_tick(tick)

	def _on_timeline_cursor_cb(self, tick: int) -> None:
		self._playback.seek_to_tick(tick)

	def _on_playback_position_df(self, tick: int) -> None:
		self._timeline.set_playback_time(tick / TICKS_PER_SECOND)

	def _on_timeline_cursor_df(self, time_sec: float) -> None:
		self._playback.seek_to_tick(int(time_sec * TICKS_PER_SECOND))

	# 属性变更

	def _on_property_changed(self, element_id: str, key: str, value: object, old_value: object = None) -> None:
		log.debug(f"属性变更: id={element_id}, {key}={value} (old={old_value})")
		elem = self._controller.get_element(element_id)
		if elem is None:
			return
		is_complex = self._controller.apply_property_change(element_id, key, value, old_value)
		if not is_complex:
			self._undo_manager.push_property_change(element_id, key, old_value, value)
		else:
			log.debug(f"复杂属性变更: id={element_id}, key={key}")
		self._inspector.refresh(elem)
		self._project_manager.mark_modified()

	# 位置选择

	def _on_position_select_requested(self, which: str) -> None:
		log.debug(f"位置选择请求: target={which}")
		self._pending_position_target = which
		self._pos_selector.showNormal()

	def _on_position_chosen(self, point: MinecraftPosition) -> None:
		log.debug(f"位置已选择: ({point.x}, {point.y}, {point.z}), target={self._pending_position_target}")
		which = getattr(self, '_pending_position_target', 'position')
		eid = self._controller.selected_id
		if not eid:
			return
		if not self._controller.set_position(eid, which, point.x, point.y, point.z):
			log.warning(f"设置位置失败: eid={eid}, target={which}")
			return
		elem = self._controller.selected_element
		self._property_panel.load_element(elem)
		self._inspector.refresh(elem)
		self._project_manager.mark_modified()

	# 项目操作

	def _on_project_opened(self, project: Project) -> None:
		log.debug(f"项目已打开: name={project.name}, backend={project.backend.value}, elements={len(project.all_elements)}, bpm={project.bpm:.0f}")

	def _on_project_settings(self) -> None:
		proj = self._project_manager.project
		dlg = ProjectSettingsDialog(proj.name,
		                            proj.bpm,
		                            proj.mc_version,
		                            proj.backend.value,
		                            proj.audio_offset_ms,
		                            proj.time_signature,
		                            self)
		if dlg.exec() == QDialog.DialogCode.Accepted:
			proj.bpm = dlg.bpm
			proj.name = dlg.project_name
			proj.mc_version = dlg.mc_version
			proj.audio_offset_ms = dlg.audio_offset_ms
			proj.time_signature = dlg.time_signature
			self._playback.set_bpm(proj.bpm)
			self._transport_bar.set_bpm(proj.bpm)
			self._timeline.update_music_info(proj.bpm, proj.audio_offset_ms, proj.time_signature, proj.ticks_per_beat)
			self._sync_metronome_settings()
			self._project_manager.mark_modified()
			log.debug(f"项目设置更新: name={proj.name}, bpm={proj.bpm:.0f}, ts={proj.time_signature}, mc_version={proj.mc_version}")
			self._ui.label.setText(f"{proj.name} - {proj.mc_version}")
			self.setWindowTitle(f"DynFirework   {proj.name}")
			self.statusBar().showMessage(f"BPM: {proj.bpm:.0f} | {proj.time_signature[0]}/{proj.time_signature[1]} | MC {proj.mc_version} | {proj.name}")

	# 窗口状态

	def _restore_window_state(self) -> None:
		settings = QSettings("DynFirework", "dyn-gui")
		geo = settings.value("mainwin/geometry")
		if geo:
			self.restoreGeometry(geo)
		state = settings.value("mainwin/state")
		if state:
			self.restoreState(state)

	def closeEvent(self, event) -> None:
		if self._project_manager.is_modified:
			reply = QMessageBox.question(
				self, "未保存的更改",
				"当前项目有未保存的更改，是否保存？",
				QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel,
			)
			if reply == QMessageBox.Save:
				log.debug("关闭窗口: 用户选择保存")
				self._on_save_project()
				if self._project_manager.is_modified:
					log.warning("关闭窗口: 保存失败，取消关闭")
					event.ignore()
					return
			elif reply == QMessageBox.Cancel:
				log.debug("关闭窗口: 用户取消")
				event.ignore()
				return
			else:
				log.debug("关闭窗口: 用户选择不保存")

		settings = QSettings("DynFirework", "dyn-gui")
		settings.setValue("mainwin/geometry", self.saveGeometry())
		settings.setValue("mainwin/state", self.saveState())
		log.debug("应用程序关闭")
		super().closeEvent(event)

def main():
	setup_logging()
	log.debug("DynFirework 启动")
	app = QApplication(sys.argv)
	app.setApplicationName("DynFirework")
	app.setOrganizationName("SparkTeam")

	# 加载资源字体
	_font_to_load = (RESOURCE_DIR / "fonts").glob("*.ttf")
	log.debug(f"加载字体: {list(_font_to_load)}")
	for _tf in _font_to_load:
		log.debug(f"加载：{_tf.name}" if QFontDatabase.addApplicationFont(str(_tf)) else f"加载失败：{_tf.name}")

	win = MainWin()
	win.showMaximized()
	sys.exit(app.exec())

if __name__ == "__main__":
	main()
