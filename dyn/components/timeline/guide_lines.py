"""时间线辅助线渲染 刻度线 + BPM节拍线 坐标系无关."""
from __future__ import annotations

import math
from typing import Callable

from PySide6.QtGui import QPainter, QPen, QColor

from .theme import TRACK_LABEL_WIDTH

def _nice_interval(min_interval: float) -> float:
	"""向上取整到易于阅读的数值: 1, 2, 5, 10, 20, 50, ..."""
	if min_interval <= 0:
		return 1.0
	magnitude = 10 ** math.floor(math.log10(min_interval))
	residual = min_interval / magnitude
	if residual <= 1:
		nice = 1
	elif residual <= 2:
		nice = 2
	elif residual <= 5:
		nice = 5
	else:
		nice = 10
	return nice * magnitude

class GuideLineRenderer:
	"""刻度线与BPM节拍线渲染器 通过注入坐标转换函数适配 tick/second 坐标系.

	CB (tick-based):   to_x=tick_to_x, from_x=x_to_tick, px_per_native=pixels_per_tick, nps=20
	DF (second-based): to_x=time_to_x, from_x=x_to_time, px_per_native=pixels_per_second, nps=1
	"""

	def __init__(self, *,
	             to_x: Callable[[float], float],
	             from_x: Callable[[float], float],
	             px_per_native: Callable[[], float],
	             native_per_second: float = 20,
	             label_width: int = TRACK_LABEL_WIDTH,
	             tick_major_color: QColor,
	             tick_minor_color: QColor,
	             beat_major_color: QColor,
	             beat_minor_color: QColor):
		self._to_x = to_x
		self._from_x = from_x
		self._px_per_native = px_per_native
		self._nps = native_per_second
		self._label_width = label_width
		self._tick_major = tick_major_color
		self._tick_minor = tick_minor_color
		self._beat_major = beat_major_color
		self._beat_minor = beat_minor_color

	def paint_tick_marks(self, p: QPainter, y_top: float, y_bot: float,
	                     widget_width: int) -> None:
		"""绘制时间刻度线."""
		major = _nice_interval(50.0 / self._px_per_native())
		minor = major / 5.0
		start = float(int(self._from_x(float(self._label_width)) / major) * major)
		end = self._from_x(float(widget_width)) + minor
		t = start
		while t <= end:
			x = int(self._to_x(t))
			if abs(t - round(t / major) * major) < major * 0.001:
				p.setPen(QPen(self._tick_major, 0))
				p.drawLine(x, int(y_top), x, int(y_bot))
			else:
				p.setPen(QPen(self._tick_minor, 0))
				p.drawLine(x, int(y_top), x, int(y_top) + 4)
			t += minor

	def paint_beat_lines(self, p: QPainter, y_top: float, y_bot: float,
	                     widget_width: int, *,
	                     bpm: float, audio_offset_ms: float,
	                     time_signature: tuple, show: bool) -> None:
		"""绘制BPM节拍线 缩放过小时自动隐藏次节拍只保留主节拍."""
		if not show or bpm <= 0:
			return
		beat_interval = (60.0 / bpm) * self._nps
		beats_per_measure = time_signature[0]
		measure_interval = beat_interval * beats_per_measure
		offset = (audio_offset_ms / 1000.0) * self._nps

		px = self._px_per_native()
		show_minor = beat_interval * px >= 10.0

		start = max(0.0, self._from_x(float(self._label_width)) - measure_interval)
		end = self._from_x(float(widget_width)) + measure_interval

		beat = int((start - offset) / beat_interval) - 1
		while True:
			pos = offset + beat * beat_interval
			if pos > end:
				break
			if pos >= start:
				x = int(self._to_x(pos))
				if self._label_width <= x <= widget_width:
					if beat % beats_per_measure == 0:
						p.setPen(QPen(self._beat_major, 3))
						p.drawLine(x, int(y_top), x, int(y_bot))
					elif show_minor:
						p.setPen(QPen(self._beat_minor, 1))
						p.drawLine(x, int(y_top), x, int(y_bot))
			beat += 1
