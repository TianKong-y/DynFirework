"""新建项目对话框 使用 new_proj_dialog.ui."""
from __future__ import annotations

import logging

from PySide6 import QtWidgets

from dyn.ui.actions.new_proj_dialog import Ui_Dialog

log = logging.getLogger(__name__)

BACKEND_MC_VERSIONS: dict[str, list[str]] = {
	"cb": ["1.12.2", "1.16.5"],
	"df": ["1.20.1", "1.20.4", "1.21", "1.21.8"],
}

class NewProjectDialog(QtWidgets.QDialog):
	"""收集新建项目参数 后端锁定后不可更改."""

	def __init__(self, parent=None) -> None:
		super().__init__(parent)
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)
		self.ui.backend_box.currentIndexChanged.connect(self._on_backend_changed)
		self._on_backend_changed()
		log.debug("打开新建项目对话框")

	def _on_backend_changed(self) -> None:
		b = self.backend
		log.debug(f"后端切换: {b}")
		versions = BACKEND_MC_VERSIONS.get(b, [])
		self.ui.mc_version_box.clear()
		# .ui 中的项目文本带 ", Forge" / ", Fabric" 后缀，但直接用 addItems 添加纯净版本号
		self.ui.mc_version_box.addItems(versions)
		if b == "df":
			idx = self.ui.mc_version_box.findText("1.21.8")
			if idx >= 0:
				self.ui.mc_version_box.setCurrentIndex(idx)

	def accept(self) -> None:
		log.debug("新建项目对话框: 用户确认")
		super().accept()

	def reject(self) -> None:
		log.debug("新建项目对话框: 用户取消")
		super().reject()

	@property
	def project_name(self) -> str:
		return self.ui.proj_name_edit.text().strip()

	@property
	def backend(self) -> str:
		return "cb" if self.ui.backend_box.currentIndex() == 1 else "df"

	@property
	def mc_version(self) -> str:
		raw = self.ui.mc_version_box.currentText()
		return raw.split(",")[0].strip()

	@property
	def bpm(self) -> float:
		return self.ui.bpm_spinbox.value()

	@property
	def namespace(self) -> str:
		return self.ui.namespace_edit.text().strip()

	@property
	def time_signature(self) -> tuple[int, int]:
		return (self.ui.time_signature_1.value(), self.ui.time_signature_2.value())

	@property
	def audio_offset_ms(self) -> int:
		return self.ui.audio_offset_spinbox.value()
