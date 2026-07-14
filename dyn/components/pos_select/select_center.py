"""位置选择器主窗口 网格/雷达双模式."""
from __future__ import annotations

import json
import sys

from dyn.logging_config import get_logger

log = get_logger(__name__)

from PySide6 import QtWidgets
from PySide6.QtCore import Signal, QItemSelectionModel
from PySide6.QtGui import QKeySequence, QColor, QUndoStack
from PySide6.QtWidgets import (
	QApplication, QMainWindow, QGridLayout, QAbstractItemView, QFileDialog,
	QMessageBox,
)

from dyn.ui.components.pos_selector.pos_selector import Ui_MainWindow as PosSelectMainUI
from dyn.lib.units import MinecraftPosition
from dyn.components.pos_select.grid_select import (
	_BaseGraphWidget, PixGraphWidget, PixElementList,
)
from dyn.components.pos_select.radar_select import RadarWidget

class PosSelectMainWindow(QMainWindow):
	"""位置选择器 网格图和雷达图共享同一数据源."""
	send_chosen_point = Signal(MinecraftPosition)

	def __init__(self) -> None:
		super().__init__()
		self._chosen_point: MinecraftPosition | None = None
		self._mode: str = "grid"

		# 共享数据源（所有位置点） 单例
		self._points: list[MinecraftPosition] = []
		self._fastsearch: set[tuple[int, int]] = set()
		self._shared_undo_stack = QUndoStack(self)

		self.ui = PosSelectMainUI()
		self.ui.setupUi(self)

		# 创建两种图形组件，共享同一数据引用
		self.pix_graph = PixGraphWidget()
		self.radar_graph = RadarWidget()

		# 注入共享数据
		self._inject_shared_data(self.pix_graph)
		self._inject_shared_data(self.radar_graph)

		# 两组件放入同一布局同一位置，显示网格、隐藏雷达
		self.pixGraphLayout = QGridLayout(self.ui.widget)
		self.pixGraphLayout.setSpacing(0)
		self.pixGraphLayout.setContentsMargins(0, 0, 0, 0)
		self.pixGraphLayout.addWidget(self.pix_graph, 0, 0)
		self.pixGraphLayout.addWidget(self.radar_graph, 0, 0)
		self.radar_graph.hide()

		self._active_graph = self.pix_graph

		# 列表模型
		self.pix_element_list = PixElementList()
		self.ui.listView_element.setModel(self.pix_element_list)
		self.ui.listView_element.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)

		self.ui.buttonBox.button(QtWidgets.QDialogButtonBox.Ok).setEnabled(False)

		self._setup_menus()
		self.signal_connect()
		self.connect_menu_toggles()

	def _inject_shared_data(self, graph: _BaseGraphWidget) -> None:
		"""将共享数据注入图形组件."""
		graph.stored_pix_list = self._points
		graph.stored_pix_fastsearch = self._fastsearch
		graph._undo_stack = self._shared_undo_stack

	@property
	def chosen_point(self) -> MinecraftPosition | None:
		return self._chosen_point

	@chosen_point.setter
	def chosen_point(self, point: MinecraftPosition | None) -> None:
		self._chosen_point = point
		self.ui.buttonBox.button(QtWidgets.QDialogButtonBox.Ok).setEnabled(point is not None)

	@property
	def mode(self) -> str:
		return self._mode

	@property
	def points(self) -> list[MinecraftPosition]:
		return self._points

	@property
	def fastsearch(self) -> set[tuple[int, int]]:
		return self._fastsearch

	def _setup_menus(self) -> None:
		ui = self.ui
		ui.grid_select_toggle.triggered.connect(lambda: self.switch_mode("grid"))
		ui.radar_graph_toggle.triggered.connect(lambda: self.switch_mode("radar"))
		ui.undo_action.setShortcut(QKeySequence.Undo)
		ui.undo_action.triggered.connect(self._on_undo)
		ui.redo_action.setShortcut(QKeySequence("Ctrl+Shift+Z"))
		ui.redo_action.triggered.connect(self._on_redo)

	def switch_mode(self, mode: str) -> None:
		log.debug(f"switch_mode {mode}")
		if mode == self._mode:
			return

		# 断开旧 graph 信号
		try:
			self._active_graph.point_renewed_sign.disconnect(self.pix_element_list.get_element_list)
			self._active_graph.selection_changed.disconnect(self.pix_element_list.get_graph_selection)
			self._active_graph.selection_changed.disconnect(self.get_chosen_point)
		except (RuntimeError, TypeError) as e:
			log.debug(f"信号断开异常: {e}")

		self._mode = mode
		if mode == "grid":
			self.radar_graph.hide()
			self.pix_graph.show()
			self._active_graph = self.pix_graph
			self.ui.grid_select_toggle.setChecked(True)
			self.ui.radar_graph_toggle.setChecked(False)
		else:
			self.pix_graph.hide()
			self.radar_graph.show()
			self._active_graph = self.radar_graph
			self.ui.grid_select_toggle.setChecked(False)
			self.ui.radar_graph_toggle.setChecked(True)

		# 重连新 graph 信号
		self._connect_graph(self._active_graph)
		self._active_graph.update()

	def _on_undo(self) -> None:
		if self._shared_undo_stack.canUndo():
			log.debug(f"位置选择器撤销: {self._shared_undo_stack.undoText()}")
			self._shared_undo_stack.undo()
			self.pix_element_list.get_element_list(self._points)
			if self._active_graph:
				self._active_graph.update()

	def _on_redo(self) -> None:
		if self._shared_undo_stack.canRedo():
			log.debug(f"位置选择器重做: {self._shared_undo_stack.redoText()}")
			self._shared_undo_stack.redo()
			self.pix_element_list.get_element_list(self._points)
			if self._active_graph:
				self._active_graph.update()

	def showEvent(self, event) -> None:
		"""窗口显示时记录日志."""
		log.debug(f"位置选择器显示: mode={self._mode}, points={len(self._points)}")
		super().showEvent(event)

	def signal_connect(self):
		# 仅连接活跃 graph 的信号（避免两套信号造成重复条目）
		self._connect_graph(self.pix_graph)
		self.pix_element_list.selection_changed.connect(self.get_chosen_point)
		self.ui.listView_element.selectionModel().selectionChanged.connect(
			self.pix_element_list.get_list_selection
		)
		log.debug("位置选择器信号已连接")

	def _connect_graph(self, graph: _BaseGraphWidget) -> None:
		graph.point_renewed_sign.connect(self.pix_element_list.get_element_list)
		graph.selection_changed.connect(self.pix_element_list.get_graph_selection)
		graph.selection_changed.connect(self.get_chosen_point)

	def connect_menu_toggles(self):
		self.ui.exit_action.triggered.connect(self.close)
		self.ui.buttonBox.rejected.connect(self.close)
		self.ui.buttonBox.accepted.connect(self.confirm_selection)
		self.ui.min_size_action.triggered.connect(self._on_min_size)
		self.ui.max_size_action.triggered.connect(self._on_max_size)
		self.ui.proper_size_action.triggered.connect(self._on_proper_size)
		self.ui.delete_point_button.clicked.connect(self._on_del_button)
		self.ui.edit_point_button.clicked.connect(self._on_edit_button)
		self.ui.delete_action.triggered.connect(self._on_del_button)
		self.ui.import_action.triggered.connect(self.import_data)
		self.ui.export_action.triggered.connect(self.export_data)
		self._shared_undo_stack.canUndoChanged.connect(self.ui.undo_action.setEnabled)
		self._shared_undo_stack.canRedoChanged.connect(self.ui.redo_action.setEnabled)

	def _on_del_button(self) -> None:
		if self._active_graph is not None and self._active_graph.selected_point is not None:
			pt = self._active_graph.selected_point
			log.debug(f"删除位置点: ({pt.x}, {pt.y}, {pt.z})")
			self._active_graph._delete_point(pt)

	def _on_edit_button(self) -> None:
		if self._active_graph is not None and self._active_graph.selected_point is not None:
			pt = self._active_graph.selected_point
			log.debug(f"编辑位置点: ({pt.x}, {pt.y}, {pt.z})")
			self._active_graph._edit_point(pt)

	def _on_min_size(self):
		if self._active_graph: self._active_graph.set_min_pix_size()

	def _on_max_size(self):
		if self._active_graph: self._active_graph.set_max_pix_size()

	def _on_proper_size(self):
		if self._active_graph: self._active_graph.set_proper_pix_size()

	def confirm_selection(self):
		if self.chosen_point:
			pt = self.chosen_point
			log.debug(f"确认位置选择: ({pt.x:.2f}, {pt.y:.2f}, {pt.z:.2f}), label={pt.label}, color=({pt.pix_color.red()},{pt.pix_color.green()},{pt.pix_color.blue()})")
			self.send_chosen_point.emit(self.chosen_point)
		self.close()

	def selection_text_change(self):
		pt = self.chosen_point
		if pt:
			self.ui.selected_point_text.setText(f"({pt.x}, {pt.y}, {pt.z})")

	def selection_point_border_change(self):
		if self._active_graph and self.chosen_point:
			self._active_graph.get_list_selected_pix(self.chosen_point)

	def get_chosen_point(self, point: MinecraftPosition):
		log.debug(f"位置选中: ({point.x:.2f}, {point.y:.2f}, {point.z:.2f}), label={point.label}")
		self.chosen_point = point
		self.handle_chosen_point()

	def handle_chosen_point(self):
		self.selection_text_change()
		self.selection_point_border_change()
		self.update_list_selection()
		has_selection = self.chosen_point is not None
		self.ui.edit_point_button.setEnabled(has_selection)
		self.ui.delete_point_button.setEnabled(has_selection)
		self.ui.delete_action.setEnabled(has_selection)
		self.ui.move_center_action.setEnabled(has_selection)

	def update_list_selection(self):
		if self.chosen_point not in self._points:
			return
		index = self._points.index(self.chosen_point)
		model_index = self.pix_element_list.index(index)
		sel_model = self.ui.listView_element.selectionModel()
		if sel_model:
			sel_model.select(model_index, QItemSelectionModel.SelectionFlag.ClearAndSelect)

	def import_data(self):
		path, _ = QFileDialog.getOpenFileName(
			self, "导入位置点", "", "JSON 文件 (*.json);;所有文件 (*.*)"
		)
		if not path:
			return
		log.debug(f"导入位置点: {path}")
		try:
			with open(path, "r", encoding="utf-8") as f:
				data = json.load(f)
			self._points.clear()
			self._fastsearch.clear()
			for item in data:
				c = item.get("color", {})
				pt = MinecraftPosition(
					x=item["x"], y=item["y"], z=item["z"],
					label=item.get("label", ""),
					main_color=QColor(c.get("r", 255), c.get("g", 255), c.get("b", 255)),
				)
				self._points.append(pt)
				self._fastsearch.add((int(pt.x), int(pt.z)))
			self.pix_element_list.get_element_list(self._points)
			if self._active_graph:
				self._active_graph.update()
		except Exception as e:
			log.error(f"导入位置点失败: {e}", exc_info=True)
			QMessageBox.warning(self, "导入失败", str(e))

	def export_data(self):
		path, _ = QFileDialog.getSaveFileName(
			self, "导出位置点", "positions.json", "JSON 文件 (*.json)"
		)
		if not path:
			return
		log.debug(f"导出位置点: {path}, 共 {len(self._points)} 个点")
		try:
			data = [{"x": p.x, "y": p.y, "z": p.z, "label": p.label,
			         "color": {"r": p.pix_color.red(), "g": p.pix_color.green(), "b": p.pix_color.blue()}}
			        for p in self._points]
			with open(path, "w", encoding="utf-8") as f:
				json.dump(data, f, ensure_ascii=False, indent=2)
		except Exception as e:
			log.error(f"导出位置点失败: {e}", exc_info=True)
			QMessageBox.warning(self, "导出失败", str(e))

if __name__ == "__main__":
	app = QApplication(sys.argv)
	win = PosSelectMainWindow()
	win.showNormal()
	sys.exit(app.exec())
