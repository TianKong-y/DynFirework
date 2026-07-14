"""项目管理器 .dyn 文件读写和项目生命周期管理."""
from __future__ import annotations

import atexit
import tempfile
from pathlib import Path

from PySide6.QtCore import QObject, Signal

from dyn.logging_config import get_logger
from dyn.models import Project, Backend

log = get_logger(__name__)

class ProjectManager(QObject):
	"""管理项目的新建、打开、保存和关闭."""

	project_opened = Signal(Project)
	project_saved = Signal(str)  # file_path
	project_modified = Signal()
	project_closed = Signal()

	def __init__(self, parent: QObject | None = None) -> None:
		super().__init__(parent)
		self._project: Project = Project()
		self._file_path: str = ""
		self._is_modified: bool = False
		self._music_temp_path: Path | None = None

	@property
	def project(self) -> Project:
		return self._project

	@property
	def file_path(self) -> str:
		return self._file_path

	@property
	def is_modified(self) -> bool:
		return self._is_modified

	@property
	def has_file(self) -> bool:
		return bool(self._file_path)

	@property
	def backend(self) -> Backend:
		return self._project.backend

	def mark_modified(self) -> None:
		self._is_modified = True
		self.project_modified.emit()

	def new_project(self, name: str = "Untitled", backend: str = "df",
	                mc_version: str = "1.21.8", bpm: float = 120.0,
	                time_signature: tuple = (4, 4), audio_offset_ms: int = 0) -> Project:
		log.debug(f"创建新项目: name={name}, backend={backend}, mc={mc_version}, bpm={bpm}, ts={time_signature}, offset={audio_offset_ms}ms")
		self._cleanup_music_temp()
		self._project = Project(
			backend=Backend(backend),
			name=name,
			mc_version=mc_version,
			bpm=bpm,
			time_signature=time_signature,
			audio_offset_ms=float(audio_offset_ms),
		)
		self._file_path = ""
		self._is_modified = False
		self.project_opened.emit(self._project)
		return self._project

	def open_project(self, path: str | Path) -> Project:
		log.debug(f"打开项目: {path}")
		self._cleanup_music_temp()
		try:
			self._project = Project.from_file(path)
		except Exception as e:
			log.error(f"无法打开项目 {path}: {e}", exc_info=True)
			raise
		self._file_path = str(path)
		self._is_modified = False
		self.project_opened.emit(self._project)
		return self._project

	def save_project(self, path: str | Path | None = None) -> bool:
		if path is not None:
			self._file_path = str(path)
		if not self._file_path:
			log.warning("保存失败: 无文件路径")
			return False
		log.debug(f"保存项目: {self._file_path}")
		try:
			self._project.to_file(self._file_path)
		except Exception as e:
			log.error(f"保存项目失败: {e}", exc_info=True)
			return False
		self._is_modified = False
		self.project_saved.emit(self._file_path)
		log.debug(f"项目已保存: {self._file_path}")
		return True

	def set_music(self, filepath: str | Path) -> bool:
		"""导入音乐文件 读取内容嵌入项目.
		Args:
			filepath: 音乐文件路径

		Returns:
			True 表示成功
		"""
		filepath = Path(filepath)
		if not filepath.is_file():
			log.warning(f"音乐文件不存在: {filepath}")
			return False
		try:
			self._project.music_data = filepath.read_bytes()
			self._project.music_original_name = filepath.name
			log.debug(
				f"导入音乐: {filepath.name} ({len(self._project.music_data)} 字节)"
			)
			self.mark_modified()
			return True
		except OSError as e:
			log.error(f"读取音乐文件失败: {e}")
			return False

	def get_music_temp_path(self) -> str | None:
		"""将嵌入的音乐数据写入临时文件，返回路径供播放器使用.

		临时文件在项目关闭或进程退出时自动清理.
		"""
		if not self._project.has_music:
			return None

		if self._music_temp_path and self._music_temp_path.exists():
			return str(self._music_temp_path)

		suffix = ""
		if self._project.music_original_name:
			suffix = Path(self._project.music_original_name).suffix
		if not suffix:
			suffix = ".mp3"

		try:
			tmp = tempfile.NamedTemporaryFile(
				suffix=suffix, delete=False, prefix="dyn_music_"
			)
			tmp.write(self._project.music_data)
			tmp.flush()
			self._music_temp_path = Path(tmp.name)
			tmp.close()
			log.debug(f"音乐临时文件: {self._music_temp_path}")
			return str(self._music_temp_path)
		except OSError as e:
			log.error(f"创建音乐临时文件失败: {e}")
			return None

	def close_project(self) -> None:
		log.debug("关闭项目")
		self._cleanup_music_temp()
		self._project = Project()
		self._file_path = ""
		self._is_modified = False
		self.project_closed.emit()

	def _cleanup_music_temp(self) -> None:
		"""清理音乐临时文件."""
		if self._music_temp_path and self._music_temp_path.exists():
			try:
				self._music_temp_path.unlink()
				log.debug(f"已清理音乐临时文件: {self._music_temp_path}")
			except OSError as e:
				log.warning(f"清理音乐临时文件失败: {self._music_temp_path}, {e}")
		self._music_temp_path = None

def _cleanup_all_temp() -> None:
	"""进程退出时清理所有残留临时文件."""
	tmp_dir = Path(tempfile.gettempdir())
	for f in tmp_dir.glob("dyn_music_*"):
		try:
			f.unlink()
		except OSError as e:
			log.warning(f"清理临时文件失败: {f}")

atexit.register(_cleanup_all_temp)
