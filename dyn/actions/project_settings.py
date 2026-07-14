"""项目设置对话框 使用 proj_settings.ui."""
from __future__ import annotations

import logging

from PySide6 import QtWidgets

from dyn.actions.new_project import BACKEND_MC_VERSIONS
from dyn.ui.actions.proj_settings import Ui_Dialog

log = logging.getLogger(__name__)

class ProjectSettingsDialog(QtWidgets.QDialog):
	"""编辑项目名称、BPM、音频偏移、拍号和 Minecraft 版本."""

	def __init__(self, name: str = "Untitled", bpm: float = 120.0,
	             mc_version: str = "1.20.1", backend: str = "df",
	             audio_offset_ms: float = 0.0, time_signature: tuple = (4, 4),
	             parent=None) -> None:
		super().__init__(parent)
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)

		self.ui.proj_name_edit.setText(name)
		self.ui.bpm_spinbox.setValue(bpm)
		self.ui.time_signature_1.setValue(time_signature[0])
		self.ui.time_signature_2.setValue(time_signature[1])
		self.ui.audio_offset_spinbox.setValue(int(audio_offset_ms))
		self.ui.backend_text.setText(
			"ColorBlock (/particleex)" if backend == "cb"
			else "DynFireworkMod v2.0 (/df)")

		versions = BACKEND_MC_VERSIONS.get(backend, BACKEND_MC_VERSIONS["df"])
		self.ui.mc_version_box.addItems(versions)
		idx = self.ui.mc_version_box.findText(mc_version)
		if idx >= 0:
			self.ui.mc_version_box.setCurrentIndex(idx)

		log.debug(f"打开项目设置: name={name}, bpm={bpm}, offset={audio_offset_ms}ms")

	def accept(self) -> None:
		log.debug("项目设置对话框: 用户确认")
		super().accept()

	def reject(self) -> None:
		log.debug("项目设置对话框: 用户取消")
		super().reject()

	@property
	def project_name(self) -> str:
		return self.ui.proj_name_edit.text().strip()

	@property
	def bpm(self) -> float:
		return self.ui.bpm_spinbox.value()

	@property
	def audio_offset_ms(self) -> float:
		return float(self.ui.audio_offset_spinbox.value())

	@property
	def time_signature(self) -> tuple[int, int]:
		return (self.ui.time_signature_1.value(), self.ui.time_signature_2.value())

	@property
	def mc_version(self) -> str:
		raw = self.ui.mc_version_box.currentText()
		return raw.split(",")[0].strip()

	@property
	def namespace(self) -> str:
		return self.ui.namespace_edit.text().strip()
