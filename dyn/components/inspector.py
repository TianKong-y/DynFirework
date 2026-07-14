"""检查器面板 以只读 JSON 显示当前选中元素 V2."""
from __future__ import annotations

import json
import logging

from PySide6.QtGui import QFontDatabase
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPlainTextEdit

from dyn.models.df.base import Element as DfElement

log = logging.getLogger("dyn.components.inspector")

class Inspector(QWidget):
	"""只读 JSON 检查器，显示选中元素的完整属性.
	标题行由 .ui 的 inspector_label + inspector_target 提供，此处仅含编辑器."""

	def __init__(self, parent: QWidget | None = None) -> None:
		super().__init__(parent)
		self._setup_ui()

	def _setup_ui(self) -> None:
		layout = QVBoxLayout(self)
		layout.setContentsMargins(0, 0, 0, 0)
		layout.setSpacing(0)

		self._editor = QPlainTextEdit()
		self._editor.setReadOnly(True)
		self._editor.setPlaceholderText("未选中任何元素")
		font = QFontDatabase.systemFont(QFontDatabase.FixedFont)
		font.setPointSize(11)
		self._editor.setFont(font)
		layout.addWidget(self._editor)

	def show_element(self, element) -> None:
		if element is None:
			log.debug("检查器: 清空")
			self._editor.setPlainText("")
			self._editor.setPlaceholderText("未选中任何元素")
			return

		name = getattr(element, 'name', '?')
		eid = getattr(element, 'id', '?')
		if isinstance(element, DfElement):
			log.debug(f"检查器: 显示元素 id={eid}, name={name}, cat={element.category.value}, time={element.start_time:.2f}s")
		else:
			log.debug(f"检查器: 显示元素 id={eid}, name={name}, tick={element.start_tick}")
		json_str = element.to_json()
		formatted = json.dumps(json_str, ensure_ascii=False, indent=2)
		log.debug(f"  数据大小: {len(formatted)} 字符")
		self._editor.setPlainText(formatted)

	def refresh(self, element) -> None:
		self.show_element(element)

	def clear(self) -> None:
		self.show_element(None)
