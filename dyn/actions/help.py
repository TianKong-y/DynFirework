"""帮助窗口 基于文件系统名的扁平化目录."""
from __future__ import annotations

import logging
from pathlib import Path

from PySide6 import QtWidgets
from PySide6.QtCore import Qt

from dyn.ui.about.help import Ui_MainWindow as HelpUI

log = logging.getLogger("dyn.actions.help")

def _display_name(name: str) -> str:
	"""从文件名提取显示名: '01. 概述/' -> '概述', '01. 什么是DynFirework.md' -> '什么是DynFirework'."""
	stem = name.rsplit('.', 1)[0] if name.endswith('.md') else name
	parts = stem.split('. ', 1) if '. ' in stem else stem.split('-', 1)
	return parts[1] if len(parts) == 2 and parts[0].isdigit() else stem

def _discover_tree(help_dir: Path, base: Path | None = None) -> list[tuple[str, str | list, str | None]]:
	"""递归扫描 help/ 目录，按文件名排序构建树形结构.
	返回 [(显示名, 相对路径 | 子节点列表, dir_path | None), ...]
	"""
	if base is None:
		base = help_dir
	items: list[tuple[str, str | list, str | None]] = []
	entries = sorted(help_dir.iterdir(), key=lambda p: (not p.is_dir(), p.name))
	for entry in entries:
		if entry.name.startswith('.'):
			continue
		if entry.is_dir():
			children = _discover_tree(entry, base)
			if children:
				items.append((_display_name(entry.name), children, str(entry.relative_to(base))))
		elif entry.suffix == '.md':
			prefix = entry.stem.split('-', 1)[0]
			if prefix.isdigit() and int(prefix) == 0:
				continue
			items.append((_display_name(entry.name), str(entry.relative_to(base)), None))
	return items

class DYNHelpWindow(QtWidgets.QMainWindow):
	"""帮助窗口 左侧扁平目录列表，右侧 Markdown 渲染."""

	_HELP_DIR: Path = Path(__file__).parent.parent / "help"

	def __init__(self) -> None:
		super().__init__()
		log.debug("打开帮助窗口")
		self.ui = HelpUI()
		self.ui.setupUi(self)

		self._populate_list(_discover_tree(self._HELP_DIR))

		self.ui.listWidget.currentItemChanged.connect(self._on_item_changed)
		self.ui.pushButton.clicked.connect(self.close)

		self.ui.listWidget.setCurrentRow(0)

	def _populate_list(self, nodes: list[tuple[str, str | list, str | None]], level: int = 0) -> None:
		for display, value, dir_path in nodes:
			if isinstance(value, list):
				item = QtWidgets.QListWidgetItem("  " * level + display)
				item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsSelectable)
				font = item.font()
				font.setBold(True)
				item.setFont(font)
				self.ui.listWidget.addItem(item)
				# 目录节点：查找 00-XXX 介绍文件
				if dir_path:
					intro_dir = self._HELP_DIR / dir_path
					for f in sorted(intro_dir.glob('00-*.md')):
						item.setData(Qt.ItemDataRole.UserRole, str(f.relative_to(self._HELP_DIR)))
						break
				self._populate_list(value, level + 1)
			else:
				item = QtWidgets.QListWidgetItem("  " * (level + 1) + display)
				item.setData(Qt.ItemDataRole.UserRole, value)
				self.ui.listWidget.addItem(item)

	def _on_item_changed(
			self,
			current: QtWidgets.QListWidgetItem,
			previous: QtWidgets.QListWidgetItem | None,  # noqa: ARG002
	) -> None:
		filename = current.data(Qt.ItemDataRole.UserRole)
		if filename:
			filepath = self._HELP_DIR / filename
			if filepath.exists():
				self.ui.textBrowser.setMarkdown(filepath.read_text(encoding="utf-8"))
			else:
				log.warning(f"帮助文档未找到: {filename}")
				self.ui.textBrowser.setPlainText("文档未找到。")
		else:
			self.ui.textBrowser.setPlainText("")
