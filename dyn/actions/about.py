"""关于对话框."""
from __future__ import annotations

import logging
import subprocess
from pathlib import Path

from PySide6 import QtWidgets
from PySide6.QtCore import QUrl
from PySide6.QtGui import QDesktopServices

from dyn import env
from dyn.ui.about.about import Ui_Dialog as AboutUI

log = logging.getLogger("dyn.actions.about")

def _resolve_version() -> str:
	dev_mode = env.get_flag(env.ENV_TEST)
	if dev_mode:
		log.debug("DYN_TEST_ENABLED=1，使用详细版本号")
	try:
		args = ["git", "describe", "--tags", "--long"] if dev_mode else ["git", "describe", "--tags", "--abbrev=0"]
		r = subprocess.run(
			args, capture_output=True, text=True,
			cwd=Path(__file__).parent.parent,
		)
		if r.returncode == 0:
			return r.stdout.strip()
	except Exception:
		log.debug("git 不可用")
	return "v1.3"

class DYNAboutWindow(QtWidgets.QDialog):
	"""关于 DynFirework 对话框."""

	_URLS: dict[str, str] = {
		"dynfirework_github_toolbutton": "https://github.com/TianKong-y/DynFirework",
		"dfmod_toolbutton": "https://github.com/TianKong-y/DynFireworkMod",
		"issue_toolbutton": "https://github.com/TianKong-y/DynFirework/issues",
		"contribute_toolbutton": "https://github.com/TianKong-y/DynFirework/pulls",
		"pyside_toolbutton": "https://www.qt.io/",
		"python_toolbutton": "https://www.python.org/",
		"minecraft_toolbutton": "https://www.minecraft.net/",
	}

	def __init__(self) -> None:
		super().__init__()
		log.debug("打开关于对话框")
		self.ui = AboutUI()
		self.ui.setupUi(self)
		self.ui.label_4.setText(_resolve_version())
		self._connect_urls()

	def _connect_urls(self) -> None:
		for obj_name, url in self._URLS.items():
			btn = getattr(self.ui, obj_name, None)
			if btn:
				btn.clicked.connect(lambda checked, u=url: QDesktopServices.openUrl(QUrl(u)))  # noqa: ARG005
