"""导出数据包对话框 使用 export_as_datapack_dialog.ui."""
from __future__ import annotations

import logging

from PySide6 import QtWidgets

from dyn.ui.actions.export_as_datapack_dialog import Ui_Dialog

log = logging.getLogger(__name__)

_MC_TO_PACK_FORMAT: dict[str, int] = {
	"1.12.2": 3,
	"1.16.5": 6,
	"1.20.1": 15,
	"1.20.4": 22,
	"1.21": 48,
	"1.21.8": 57,
}

def _resolve_pack_format(mc_version: str) -> int:
	fmt = _MC_TO_PACK_FORMAT.get(mc_version)
	if fmt is None:
		log.warning(f"未知 MC 版本: {mc_version}, 使用默认 pack_format")
		return 48
	return fmt

class ExportDatapackDialog(QtWidgets.QDialog):
	"""收集数据包导出参数."""

	def __init__(self, default_name: str = "DynFirework", mc_version: str = "1.21.8", parent=None) -> None:
		super().__init__(parent)
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)
		self.ui.datapack_name_edit.setText(default_name)
		self.ui.mc_version_text.setText(f"MC {mc_version}")
		self.ui.pack_format_number.setText(str(_resolve_pack_format(mc_version)))
		log.debug("打开导出对话框")

	def accept(self) -> None:
		log.debug("导出对话框: 用户确认")
		super().accept()

	def reject(self) -> None:
		log.debug("导出对话框: 用户取消")
		super().reject()

	@property
	def pack_name(self) -> str:
		return self.ui.datapack_name_edit.text().strip()

	@property
	def namespace(self) -> str:
		ns = self.ui.namespace_edit.text().strip()
		return ns if ns else ""

	@property
	def description(self) -> str:
		return self.ui.textEdit.toPlainText().strip()

	@property
	def pack_format(self) -> int:
		try:
			return int(self.ui.pack_format_number.text())
		except ValueError:
			return 48
