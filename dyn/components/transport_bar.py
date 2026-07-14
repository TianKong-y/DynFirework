"""播放控制逻辑 - 绑定 Designer .ui 中预设的传输栏控件."""
from __future__ import annotations

from PySide6.QtCore import QObject, Signal, Slot
from PySide6.QtWidgets import QToolButton, QLabel, QSlider

from dyn.logging_config import get_logger
from dyn.service.playback_controller import PlaybackController

log = get_logger(__name__)

class TransportBar(QObject):
	"""播放传输控制逻辑 - 控件由 Designer .ui 提供."""

	beat_lines_toggled = Signal(bool)
	time_marks_toggled = Signal(bool)
	metronome_toggled = Signal(bool)

	def __init__(
			self,
			controller: PlaybackController,
			btn_play: QToolButton,
			btn_stop: QToolButton,
			btn_replay: QToolButton,
			btn_hint_tick: QToolButton,
			btn_time_tick: QToolButton,
			label_time: QLabel,
			label_tick: QLabel,
			slider_volume: QSlider,
			label_music: QLabel,
			label_bpm: QLabel,
			btn_metronome: QToolButton | None = None,
			parent: QObject | None = None,
	) -> None:
		super().__init__(parent)
		self._controller = controller
		self._btn_play = btn_play
		self._btn_stop = btn_stop
		self._btn_replay = btn_replay
		self._btn_hint_tick = btn_hint_tick
		self._btn_time_tick = btn_time_tick
		self._label_time = label_time
		self._label_tick = label_tick
		self._slider_volume = slider_volume
		self._label_music = label_music
		self._label_bpm = label_bpm
		self._btn_metronome = btn_metronome
		self._setup_connections()

	def _setup_connections(self) -> None:
		self._btn_play.clicked.connect(self._controller.toggle_play_pause)
		self._btn_stop.clicked.connect(self._controller.stop)
		self._btn_replay.clicked.connect(lambda: self._controller.seek_to_tick(0))
		self._btn_hint_tick.toggled.connect(self.beat_lines_toggled.emit)
		self._btn_time_tick.toggled.connect(self.time_marks_toggled.emit)
		if self._btn_metronome is not None:
			self._btn_metronome.toggled.connect(self.metronome_toggled.emit)
		self._slider_volume.valueChanged.connect(self._on_volume_changed)
		self._controller.position_changed.connect(self._on_position_changed)
		self._controller.state_changed.connect(self._on_state_changed)

	@Slot(int)
	def _on_position_changed(self, tick: int) -> None:
		total_seconds = tick // 20
		minutes = total_seconds // 60
		secs = total_seconds % 60
		self._label_time.setText(f"{minutes:02d}:{secs:02d}")
		self._label_tick.setText(f"Tick: {tick}")

	@Slot(str)
	def _on_state_changed(self, state: str) -> None:
		if state == "playing":
			self._btn_play.setText("")
		else:
			self._btn_play.setText("▶")

	@Slot(int)
	def _on_volume_changed(self, value: int) -> None:
		audio = self._controller.player.audioOutput()
		if audio:
			audio.setVolume(value / 100.0)
		else:
			log.warning("音量变更: audioOutput() 返回 None")

	def set_bpm(self, bpm: float) -> None:
		self._label_bpm.setText(f"BPM: {bpm:.0f}")

	def set_music_path(self, path: str) -> None:
		self._label_music.setText(path if path else "")
