"""统一环境变量访问模块 提供日志记录."""

import logging
import os
import sys
from importlib.resources import files
from pathlib import Path

_log = logging.getLogger("dyn.env")

ENV_LOG_LEVEL = "DYN_LOG_LEVEL"
ENV_LOG_FILE = "DYN_LOG_FILE"
ENV_TEST = "DYN_TEST_ENABLED"

def _resolve_resources() -> Path:
	"""返回 resources 目录路径 兼容开发和 pip install 后运行."""
	try:
		return Path(str(files("dyn") / "resources"))
	except Exception:
		return Path(__file__).parent / "resources"

RESOURCE_DIR = _resolve_resources()

def get_str(name: str, default: str = "") -> str:
	val = os.environ.get(name, "")
	if val:
		_log.debug(f"env {name}={val}")
	return val or default

def get_flag(name: str) -> bool:
	val = os.environ.get(name, "")
	if val == "1":
		_log.debug(f"env {name}=1 (enabled)")
		return True
	return False

# 日志级别：在 logging 初始化前只能输出到 stderr
def resolve_console_level() -> int:
	raw = os.environ.get(ENV_LOG_LEVEL, "").strip().lower()
	if not raw:
		return logging.INFO
	level_map = {
		"debug": logging.DEBUG,
		"info": logging.INFO,
		"warning": logging.WARNING,
		"warn": logging.WARNING,
		"error": logging.ERROR,
		"critical": logging.CRITICAL,
	}
	lvl = level_map.get(raw)
	if lvl is not None:
		return lvl
	print(f"env: invalid {ENV_LOG_LEVEL}='{raw}'", file=sys.stderr)
	return logging.INFO
