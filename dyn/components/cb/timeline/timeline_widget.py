"""时间线编辑器 音频波形 + 烟花/轨迹双轨道 (cb, tick-based)."""
from __future__ import annotations

import logging
from typing import Any

from PySide6.QtCore import Qt, Signal, QEvent
from PySide6.QtGui import (
	QPainter, QPen,
	QMouseEvent, QWheelEvent, QKeyEvent, QResizeEvent,
)
from PySide6.QtWidgets import QWidget

from dyn.components.timeline.waveform import _WaveformWidget
from dyn.models.cb import Element, ElementType
from dyn.service.element_controller import ElementController
from .header import _HeaderWidget
from .overlay import _CursorOverlayWidget
from .theme import (
	palette_colors, propagate_palette,
	HEADER_HEIGHT, TRACK_LABEL_WIDTH, WAVEFORM_HEIGHT, PIXELS_PER_TICK_DEFAULT,
)
from .track_area import _TFProxy, _TrackArea

log = logging.getLogger("dyn.components.timeline")

class ParticleexTimelineWidget(QWidget):
	"""时间线编辑器 音频波形 + 烟花/轨迹双轨道 (cb)."""
	element_selected = Signal(str)
	element_moved = Signal(str, int, int)
	element_resized = Signal(str, int, int)
	playback_cursor_changed = Signal(int)
	view_changed = Signal()
	delete_requested = Signal()

	def __init__(self, parent=None) -> None:
		super().__init__(parent)
		self._controller: ElementController | None = None
		self._pixels_per_tick: float = PIXELS_PER_TICK_DEFAULT
		self._scroll_offset: float = 0.0
		self._elements: list[Element] = []
		self._selected_id: str = ""
		self._playback_tick: int = 0
		self._waveform_samples: list[float] | None = None
		self._bpm: float = 120.0
		self._audio_offset_ms: float = 0.0
		self._time_signature: tuple = (4, 4)
		self._ticks_per_beat: int = 20
		self._show_beat_lines: bool = True
		self._show_time_marks: bool = True

		self._update_colors()

		self._header = _HeaderWidget(self)
		self._header._timeline = self
		self._waveform = _WaveformWidget(self)
		self._fw_track = _TrackArea("烟花", self)
		self._traj_track = _TrackArea("轨迹", self)
		self._fw_track.drag_update.connect(self._traj_track.compute_and_update)
		self._traj_track.drag_update.connect(self._fw_track.compute_and_update)
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
		if self._controller:
			try:
				self._controller.element_added.disconnect(self._on_elements_changed)
			except (TypeError, RuntimeError):
				pass
			try:
				self._controller.element_removed.disconnect(self._on_elements_changed)
			except (TypeError, RuntimeError):
				pass
			try:
				self._controller.element_changed.disconnect(self._on_element_updated)
			except (TypeError, RuntimeError):
				pass
			try:
				self._controller.selection_changed.disconnect(self._on_selection_changed)
			except (TypeError, RuntimeError):
				pass
		self._controller = controller
		controller.element_added.connect(self._on_elements_changed)
		controller.element_removed.connect(self._on_elements_changed)
		controller.element_changed.connect(self._on_element_updated)
		controller.selection_changed.connect(self._on_selection_changed)
		log.debug("已连接 CB 控制器信号")

	def set_pixels_per_tick(self, ppt: float) -> None:
		self._pixels_per_tick = max(0.5, min(20.0, ppt))
		self._refresh_tracks()
		self.view_changed.emit()

	def set_playback_tick(self, tick: int, auto_scroll: bool = True) -> None:
		self._playback_tick = tick
		if auto_scroll:
			cx = self.tick_to_x(tick)
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
		self._ticks_per_beat = ticks_per_beat
		self.update()

	def set_show_beat_lines(self, visible: bool) -> None:
		self._show_beat_lines = visible
		self.update()

	def set_show_time_marks(self, visible: bool) -> None:
		self._show_time_marks = visible
		self.update()

	def seek_playback(self, tick: int) -> None:
		self._playback_tick = tick
		self.update()

	@property
	def playback_tick(self) -> int:
		return self._playback_tick

	@property
	def fw_track(self):
		return self._fw_track

	@property
	def traj_track(self):
		return self._traj_track

	@property
	def pixels_per_tick(self) -> float:
		return self._pixels_per_tick

	def tick_to_x(self, tick: float) -> float:
		return TRACK_LABEL_WIDTH + tick * self._pixels_per_tick - self._scroll_offset

	def x_to_tick(self, x: float) -> float:
		return max(0.0, (x - TRACK_LABEL_WIDTH + self._scroll_offset) / self._pixels_per_tick)

	def _refresh_tracks(self) -> None:
		traj: list[Element] = [e for e in self._elements if e.element_type == ElementType.TRAJECTORY]
		fw: list[Element] = [e for e in self._elements if e.element_type == ElementType.FIREWORK]
		for tf in self._elements:
			if tf.element_type != ElementType.TRAJ_FIREWORK:
				continue
			traj.append(_TFProxy(tf, "traj"))
			fw.append(_TFProxy(tf, "fw"))
		self._fw_track.set_data(fw, self._pixels_per_tick, self._scroll_offset)
		self._traj_track.set_data(traj, self._pixels_per_tick, self._scroll_offset)
		self._waveform.set_view(self._pixels_per_tick, self._scroll_offset)

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
		remaining = max(self.height() - y, 80)
		half = remaining // 2
		self._fw_track.setGeometry(0, y, w, half)
		y += half
		self._traj_track.setGeometry(0, y, w, remaining - half)
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
				tick = int(self.x_to_tick(x))
				self._playback_tick = max(0, tick)
				self.playback_cursor_changed.emit(self._playback_tick)
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
			tick = int(self.x_to_tick(event.position().x()))
			self._playback_tick = max(0, tick)
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
			self.playback_cursor_changed.emit(self._playback_tick)
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
			old = self._pixels_per_tick
			if not pixel.isNull():
				factor = 1.0 + abs(v_delta) / 600.0
				factor = max(0.9, min(1.12, factor))
			else:
				factor = 1.15
			if v_delta > 0:
				self.set_pixels_per_tick(old * factor)
			else:
				self.set_pixels_per_tick(old / factor)
			self._scroll_offset = max(0, self._playback_tick * (self._pixels_per_tick - old) + self._scroll_offset)
			log.debug(f"时间线缩放: ppt={self._pixels_per_tick:.2f}")
			self._refresh_tracks()
			self.view_changed.emit()
			self.update()

		event.accept()

	def keyPressEvent(self, event: QKeyEvent) -> None:
		if event.key() == Qt.Key_Delete and self._selected_id and self._controller:
			elem_name = next((getattr(e, 'name', '?') for e in self._elements if e.id == self._selected_id), '?')
			log.debug(f"时间线按键删除: id={self._selected_id}, name={elem_name}")
			self.delete_requested.emit()
		super().keyPressEvent(event)

	def on_elements_changed(self, *args) -> None:
		if self._controller:
			self._elements = list(self._controller.all_elements)
		log.debug(f"时间线元素更新: {len(self._elements)} 个元素")
		self._refresh_tracks()

	def _on_elements_changed(self, *args) -> None:
		self.on_elements_changed(*args)

	def _on_element_updated(self, element_id: str, key: str, value: Any) -> None:
		self._refresh_tracks()

	def _on_selection_changed(self, element_id: str) -> None:
		self._selected_id = element_id
		self._fw_track.set_selection(element_id)
		self._traj_track.set_selection(element_id)

	def _on_track_selected(self, element_id: str) -> None:
		self._selected_id = element_id
		self._fw_track.set_selection(element_id)
		self._traj_track.set_selection(element_id)
		self.element_selected.emit(element_id)

	def _on_track_moved(self, eid: str, tick: int) -> None:
		log.debug(f"轨道移动: id={eid}, new_start_tick={tick}")
		self.element_moved.emit(eid, tick)

	def _on_track_resized(self, eid: str, dur: int) -> None:
		self.element_resized.emit(eid, dur)
