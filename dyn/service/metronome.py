"""节拍器 在播放时按节拍播放主/次提示音 使用预测式调度保证均匀."""
from __future__ import annotations

from PySide6.QtCore import QObject, QUrl, Slot, QTimer, Qt, QElapsedTimer
from PySide6.QtMultimedia import QSoundEffect

from dyn.env import RESOURCE_DIR
from dyn.logging_config import get_logger

log = get_logger(__name__)

class Metronome(QObject):
	"""节拍器：根据 BPM 和拍号在对应位置播放主/次节拍音频.

	使用预测式调度：每个节拍触发后立即计算并预约下一次节拍，
	确保节拍间隔严格均匀，不依赖外部轮询时钟。
	on_tick() 仅用于初始同步和偶尔的漂移校正。"""

	def __init__(self, parent: QObject | None = None) -> None:
		super().__init__(parent)
		self._enabled: bool = False
		self._bpm: float = 120.0
		self._time_signature: tuple[int, int] = (4, 4)
		self._audio_offset_ms: float = 0.0

		self._active: bool = False
		self._scheduled_beat: int = -1
		self._playing: bool = False
		self._last_tick: int = 0
		self._tick_timer = QElapsedTimer()

		self._beat_timer = QTimer(self)
		self._beat_timer.setSingleShot(True)
		self._beat_timer.setTimerType(Qt.TimerType.PreciseTimer)
		self._beat_timer.timeout.connect(self._on_beat_timeout)

		self._primary = QSoundEffect()
		self._secondary = QSoundEffect()
		self._primary.setVolume(0.8)
		self._secondary.setVolume(0.5)

		audio_dir = RESOURCE_DIR / "audio"
		p = str((audio_dir / "metronome_primary.wav").resolve())
		s = str((audio_dir / "metronome_secondary.wav").resolve())
		self._primary.setSource(QUrl.fromLocalFile(p))
		self._secondary.setSource(QUrl.fromLocalFile(s))
		log.debug(f"节拍器音频加载: primary={p}, secondary={s}")

	@property
	def enabled(self) -> bool:
		return self._enabled

	@enabled.setter
	def enabled(self, value: bool) -> None:
		self._enabled = value
		log.debug(f"节拍器: {'启用' if value else '禁用'}")
		if not value:
			self._deactivate()

	def set_bpm(self, bpm: float) -> None:
		self._bpm = bpm
		self._deactivate()
		log.debug(f"节拍器 BPM: {bpm:.0f}")

	def set_time_signature(self, ts: tuple[int, int]) -> None:
		self._time_signature = ts
		self._deactivate()
		log.debug(f"节拍器 拍号: {ts[0]}/{ts[1]}")

	def set_audio_offset_ms(self, offset_ms: float) -> None:
		self._audio_offset_ms = offset_ms
		self._deactivate()
		log.debug(f"节拍器 音频偏移: {offset_ms:.0f}ms")

	@Slot(int)
	def on_tick(self, tick: int) -> None:
		"""从 playback 轮询回调 用于初始同步和漂移校正."""
		if not self._enabled or self._bpm <= 0 or not self._playing:
			return

		self._last_tick = tick
		self._tick_timer.restart()

		offset_ticks = (self._audio_offset_ms / 1000.0) * 20.0
		effective_tick = tick - offset_ticks
		if effective_tick < 0:
			self._deactivate()
			return

		beat_interval_ticks = (60.0 / self._bpm) * 20.0
		current_beat = int(effective_tick / beat_interval_ticks)

		if not self._active:
			self._schedule_from(current_beat)
			return

		# 漂移校正：节拍器偏离超过 1 拍时仅调整序号 不重启计时器
		diff = current_beat - self._scheduled_beat
		if diff > 1:
			log.debug(f"节拍器落后校正: scheduled={self._scheduled_beat}, actual={current_beat}")
			self._scheduled_beat = current_beat + 1
		elif diff < -1:
			log.debug(f"节拍器超前校正: scheduled={self._scheduled_beat}, actual={current_beat}")
			self._scheduled_beat = current_beat + 1

	def notify_state(self, state: str) -> None:
		"""接收播放状态变更 停止/暂停时关闭节拍器."""
		if state == "playing":
			self._playing = True
		else:
			self._playing = False
			self._deactivate()

	def _schedule_from(self, current_beat: int) -> None:
		"""从 current_beat 起预约下一个节拍 用 QElapsedTimer 获取亚 tick 精度时间."""
		next_beat = current_beat + 1
		self._scheduled_beat = next_beat
		self._active = True

		beat_interval_ms = 60000.0 / self._bpm
		next_beat_ms = self._audio_offset_ms + next_beat * beat_interval_ms

		# 用 _last_tick + QElapsedTimer 内插获取精确当前毫秒
		now_ms = self._last_tick * 50.0 + self._tick_timer.elapsed()
		delay_ms = max(0, int(next_beat_ms - now_ms))

		self._beat_timer.start(delay_ms)

	def _on_beat_timeout(self) -> None:
		"""预约的节拍到达 先预约下一拍再播放音频 避免 play() 延迟累积."""
		if not self._active:
			return

		beat = self._scheduled_beat
		if beat < 0:
			self._deactivate()
			return

		# 先预约下一拍 避免 QSoundEffect.play() 延迟影响节拍间隔
		self._scheduled_beat = beat + 1
		beat_interval_ms = int(60000.0 / self._bpm)
		self._beat_timer.start(beat_interval_ms)

		if beat % self._time_signature[0] == 0:
			self._primary.play()
		else:
			self._secondary.play()

	def _deactivate(self) -> None:
		self._active = False
		self._scheduled_beat = -1
		self._beat_timer.stop()
