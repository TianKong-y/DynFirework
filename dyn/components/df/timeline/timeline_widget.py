"""时间线编辑器 音频波形 + 烟花/轨迹/效果/复合四轨道 (df, second-based)."""
from __future__ import annotations

from typing import Any

from PySide6.QtCore import Qt, Signal, QEvent
from PySide6.QtGui import (
	QPainter, QPen,
	QMouseEvent, QWheelEvent, QKeyEvent, QResizeEvent,
)
from PySide6.QtWidgets import QWidget

from dyn.logging_config import get_logger
from dyn.models.df.base import Element as DfElement
from dyn.service.element_controller import ElementController
from .header import _HeaderWidget
from .overlay import _CursorOverlayWidget
from .proxy import create_track_views
from .theme import (
	palette_colors, propagate_palette,
	HEADER_HEIGHT, TRACK_LABEL_WIDTH, WAVEFORM_HEIGHT,
	PIXELS_PER_SECOND_DEFAULT,
	TICKS_PER_SECOND,
)
from .track_area import _TrackArea
from ...timeline.waveform import _WaveformWidget

log = get_logger(__name__)

class DFTimelineWidget(QWidget):
	"""时间线编辑器 音频波形 + 烟花/轨迹/效果/复合四轨道 (df)."""
	element_selected = Signal(str)
	element_moved = Signal(str, float, float)
	element_resized = Signal(str, float, float)
	playback_cursor_changed = Signal(float)
	view_changed = Signal()
	delete_requested = Signal()

	def __init__(self, parent=None) -> None:
		super().__init__(parent)
		self._controller: ElementController | None = None
		self._pixels_per_second: float = PIXELS_PER_SECOND_DEFAULT
		self._scroll_offset: float = 0.0
		self._elements: list[DfElement] = []
		self._selected_id: str = ""
		self._playback_time: float = 0.0

		self._waveform_samples: list[float] | None = None
		self._bpm: float = 120.0
		self._audio_offset_ms: float = 0.0
		self._time_signature: tuple = (4, 4)
		self._show_beat_lines: bool = True
		self._show_time_marks: bool = True

		self._update_colors()

		self._header = _HeaderWidget(self)
		self._header._timeline = self
		self._waveform = _WaveformWidget(self)
		self._fw_track = _TrackArea("烟花", self)
		self._traj_track = _TrackArea("轨迹", self)
		self._effect_track = _TrackArea("效果", self)
		self._composite_track = _TrackArea("复合", self)

		all_tracks = [self._fw_track, self._traj_track, self._effect_track, self._composite_track]
		for src in all_tracks:
			for dst in all_tracks:
				if src is not dst:
					src.drag_update.connect(dst.compute_and_update)

		for track in all_tracks:
			track.element_selected.connect(self._on_track_selected)
			track.element_moved.connect(self._on_track_moved)
			track.element_resized.connect(self._on_track_resized)

		self._overlay_cursor = _CursorOverlayWidget(self)
		self._overlay_cursor._timeline = self

		self._dragging_cursor: bool = False
		self._panning: bool = False
		self._pan_start_x: float = 0.0

		self.setMouseTracking(True)
		self.setFocusPolicy(Qt.StrongFocus)
		self.setMinimumHeight(120)

	@property
	def elements(self):
		return self._elements

	@property
	def fw_track(self):
		return self._fw_track

	@property
	def traj_track(self):
		return self._traj_track

	@property
	def effect_track(self):
		return self._effect_track

	@property
	def composite_track(self):
		return self._composite_track

	@fw_track.setter
	def fw_track(self, value):
		self._fw_track = value

	@traj_track.setter
	def traj_track(self, value):
		self._traj_track = value

	@effect_track.setter
	def effect_track(self, value):
		self._effect_track = value

	@composite_track.setter
	def composite_track(self, value):
		self._composite_track = value

	@property
	def pixels_per_second(self) -> float:
		return self._pixels_per_second

	@property
	def playback_time(self) -> float:
		return self._playback_time

	def _update_colors(self):
		c = palette_colors()
		self._bg_color = c["bg_dark"]
		self._waveform_color = c["highlight_alpha"]
		self._text_color = c["text"]
		self._divider_color = c["mid"]

	def changeEvent(self, event):
		if event.type() == QEvent.PaletteChange:
			self._update_colors()
			propagate_palette(self)
			self.update()
		super().changeEvent(event)

	def set_controller(self, controller: ElementController) -> None:
		if self._controller is not None:
			try:
				self._controller.element_added.disconnect(self.on_elements_changed)
				self._controller.element_removed.disconnect(self.on_elements_changed)
				self._controller.element_changed.disconnect(self._on_element_updated)
				self._controller.selection_changed.disconnect(self._on_selection_changed)
			except (TypeError, RuntimeError):
				pass
		self._controller = controller
		controller.element_added.connect(self.on_elements_changed)
		controller.element_removed.connect(self.on_elements_changed)
		controller.element_changed.connect(self._on_element_updated)
		controller.selection_changed.connect(self._on_selection_changed)
		log.debug("已连接 DF 控制器信号")

	def set_pixels_per_second(self, pps: float) -> None:
		self._pixels_per_second = max(10.0, min(400.0, pps))
		self._refresh_tracks()
		self.view_changed.emit()

	def set_playback_time(self, t: float, auto_scroll: bool = True) -> None:
		self._playback_time = t
		if auto_scroll:
			cx = self.time_to_x(t)
			visible_w = self.width()
			margin = 60
			if cx > visible_w - margin:
				self._scroll_offset += cx - visible_w + margin
				self._refresh_tracks()
				self.view_changed.emit()
			elif cx < TRACK_LABEL_WIDTH + margin:
				self._scroll_offset = max(0, self._scroll_offset - (TRACK_LABEL_WIDTH + margin - cx))
				self._refresh_tracks()
				self.view_changed.emit()
		self.update()

	def set_playback_tick(self, tick: int, auto_scroll: bool = True) -> None:
		"""兼容旧 tick 接口，内部转换为秒."""
		self.set_playback_time(tick / float(TICKS_PER_SECOND), auto_scroll)

	def set_waveform_data(self, samples: list[float] | None, sample_rate: int = 44100, bpm: float = 120.0) -> None:
		if samples:
			log.debug(f"波形数据加载: {len(samples)} samples, sr={sample_rate}, bpm={bpm:.0f}")
		self._waveform_samples = samples
		self._waveform.set_samples(samples, sample_rate, bpm)
		self._layout_children()
		self.update()

	def update_music_info(self,
	                      bpm: float,
	                      audio_offset_ms: float,
	                      time_signature: tuple = (4, 4),
	                      ticks_per_beat: int = 20) -> None:
		self._bpm = bpm
		self._audio_offset_ms = audio_offset_ms
		self._time_signature = time_signature
		self.update()

	def set_show_beat_lines(self, visible: bool) -> None:
		self._show_beat_lines = visible
		self.update()

	def set_show_time_marks(self, visible: bool) -> None:
		self._show_time_marks = visible
		self.update()

	def seek_playback(self, time_sec: float) -> None:
		self._playback_time = time_sec
		self.update()

	def time_to_x(self, t: float) -> float:
		return TRACK_LABEL_WIDTH + t * self._pixels_per_second - self._scroll_offset

	def x_to_time(self, x: float) -> float:
		return max(0.0, (x - TRACK_LABEL_WIDTH + self._scroll_offset) / self._pixels_per_second)

	def _refresh_tracks(self) -> None:
		views = create_track_views(self._elements)
		self._fw_track.set_data(views["fw"], self._pixels_per_second, self._scroll_offset)
		self._traj_track.set_data(views["traj"], self._pixels_per_second, self._scroll_offset)
		self._effect_track.set_data(views["effect"], self._pixels_per_second, self._scroll_offset)
		self._composite_track.set_data(views["composite"], self._pixels_per_second, self._scroll_offset)
		self._waveform.set_view(self._pixels_per_second / TICKS_PER_SECOND, self._scroll_offset)

	def resizeEvent(self, event: QResizeEvent) -> None:
		self._layout_children()
		super().resizeEvent(event)

	def _layout_children(self) -> None:
		w = self.width()
		y = 0
		self._header.setGeometry(0, y, w, HEADER_HEIGHT)
		y += HEADER_HEIGHT
		self._waveform.setGeometry(0, y, w, WAVEFORM_HEIGHT)
		y += WAVEFORM_HEIGHT
		remaining = max(self.height() - y, 160)
		h = remaining // 4
		extra = remaining - h * 4
		self._fw_track.setGeometry(0, y, w, h + (1 if extra > 0 else 0))
		y += h + (1 if extra > 0 else 0)
		extra -= 1
		self._traj_track.setGeometry(0, y, w, h + (1 if extra > 0 else 0))
		y += h + (1 if extra > 0 else 0)
		extra -= 1
		self._effect_track.setGeometry(0, y, w, h + (1 if extra > 0 else 0))
		y += h + (1 if extra > 0 else 0)
		self._composite_track.setGeometry(0, y, w, h + (1 if extra > 1 else 0))
		self._overlay_cursor.setGeometry(0, 0, w, self.height())
		self._overlay_cursor.raise_()

	def paintEvent(self, event) -> None:
		p = QPainter(self)
		p.setRenderHint(QPainter.Antialiasing)
		try:
			div_y = self._waveform.geometry().bottom()
			p.setPen(QPen(self._divider_color, 1))
			p.drawLine(TRACK_LABEL_WIDTH, div_y, self.width(), div_y)
		finally:
			p.end()

	def mousePressEvent(self, event: QMouseEvent) -> None:
		if event.button() == Qt.MiddleButton:
			self._panning = True
			self._pan_start_x = event.position().x()
			self.setCursor(Qt.ClosedHandCursor)
			return
		if event.button() == Qt.LeftButton:
			x = event.position().x()
			if x > TRACK_LABEL_WIDTH:
				self._playback_time = max(0.0, self.x_to_time(x))
				self.playback_cursor_changed.emit(self._playback_time)
				self._dragging_cursor = True
				self.update()
				return

	def mouseMoveEvent(self, event: QMouseEvent) -> None:
		if self._panning:
			dx = event.position().x() - self._pan_start_x
			self._scroll_offset = max(0, self._scroll_offset - dx)
			self._pan_start_x = event.position().x()
			self._refresh_tracks()
			self.view_changed.emit()
			self.update()
			return
		if self._dragging_cursor:
			t = self.x_to_time(event.position().x())
			self._playback_time = max(0.0, t)
			x = event.position().x()
			margin = 40
			if x > self.width() - margin:
				self._scroll_offset += (x - self.width() + margin)
				self._refresh_tracks()
				self.view_changed.emit()
			elif x < TRACK_LABEL_WIDTH + margin:
				self._scroll_offset = max(0, self._scroll_offset - (TRACK_LABEL_WIDTH + margin - x))
				self._refresh_tracks()
				self.view_changed.emit()
			self.playback_cursor_changed.emit(self._playback_time)
			self.update()

	def mouseReleaseEvent(self, event: QMouseEvent) -> None:
		self.setCursor(Qt.ArrowCursor)

	def mouseDoubleClickEvent(self, event: QMouseEvent) -> None:
		pass

	def wheelEvent(self, event: QWheelEvent) -> None:
		pixel = event.pixelDelta()
		angle = event.angleDelta()

		h_delta = 0
		if not pixel.isNull() and pixel.x() != 0:
			h_delta = pixel.x()
		elif angle.x() != 0:
			h_delta = angle.x()

		v_delta = 0
		if not pixel.isNull() and pixel.y() != 0:
			v_delta = pixel.y()
		elif angle.y() != 0:
			v_delta = angle.y()

		if h_delta != 0:
			self._scroll_offset = max(0, self._scroll_offset - h_delta)
			self._refresh_tracks()
			self.view_changed.emit()
			self.update()

		if event.modifiers() & Qt.ShiftModifier:
			if v_delta != 0:
				self._scroll_offset = max(0, self._scroll_offset - v_delta)
				self._refresh_tracks()
				self.view_changed.emit()
				self.update()
			event.accept()
			return

		if v_delta != 0:
			old = self._pixels_per_second
			if not pixel.isNull():
				factor = 1.0 + abs(v_delta) / 600.0
				factor = max(0.9, min(1.12, factor))
			else:
				factor = 1.15
			if v_delta > 0:
				self.set_pixels_per_second(old * factor)
			else:
				self.set_pixels_per_second(old / factor)
			log.debug(f"缩放: pps {old:.1f} -> {self._pixels_per_second:.1f}")
			self._scroll_offset = max(0, self._playback_time * (self._pixels_per_second - old) + self._scroll_offset)
			self._refresh_tracks()
			self.view_changed.emit()
			self.update()

		event.accept()

	def keyPressEvent(self, event: QKeyEvent) -> None:
		if event.key() == Qt.Key_Delete and self._selected_id and self._controller:
			log.debug(f"时间线按键删除: id={self._selected_id}")
			self.delete_requested.emit()
		super().keyPressEvent(event)

	def on_elements_changed(self, *args) -> None:
		if self._controller:
			self._elements = list(self._controller.all_elements)
		log.debug(f"时间线元素更新: {len(self._elements)} 个元素")
		self._refresh_tracks()

	def _on_element_updated(self, element_id: str, key: str, value: Any) -> None:
		self._refresh_tracks()

	def _on_selection_changed(self, element_id: str) -> None:
		self._selected_id = element_id
		for track in [self._fw_track, self._traj_track, self._effect_track, self._composite_track]:
			track.set_selection(element_id)

	def _on_track_selected(self, element_id: str) -> None:
		self._selected_id = element_id
		for track in [self._fw_track, self._traj_track, self._effect_track, self._composite_track]:
			track.set_selection(element_id)
		self.element_selected.emit(element_id)

	def _on_track_moved(self, eid: str, new_start: float, old_start: float) -> None:
		log.debug(f"轨道移动: id={eid[:8]}, {old_start:.2f}s -> {new_start:.2f}s")
		self.element_moved.emit(eid, new_start, old_start)

	def _on_track_resized(self, eid: str, new_dur: float, old_dur: float) -> None:
		self.element_resized.emit(eid, new_dur, old_dur)
