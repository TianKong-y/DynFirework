"""烟花表单共享基类 提供位置 + 内外层颜色."""
from __future__ import annotations

import logging

from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
	QWidget, QVBoxLayout, QHBoxLayout, QFormLayout,
	QLabel, QDoubleSpinBox, QCheckBox, QPushButton, QGroupBox, QDial,
)

from dyn.components.base.color_picker import ColorPicker
from dyn.components.base.form_base import FormBase
from dyn.models.cb import Element, FireworkElement, TrajFireworkElement, Position, ColorRGB

_fw_log = logging.getLogger("dyn.components.cb.fw_base")

class FwBase(FormBase):
	"""烟花表单共享基类 子类只需实现 _setup_type_sections 和 _load_type_sections."""

	property_changed = Signal(str, str, object, object)
	position_select_requested = Signal(str)

	def __init__(self, parent: QWidget | None = None) -> None:
		super().__init__(parent)
		self._element: Element | None = None
		self._loading: bool = False

		layout = QVBoxLayout(self)
		layout.setContentsMargins(0, 0, 0, 0)
		layout.setSpacing(8)

		self._setup_position()
		self._setup_inner_color()
		self._setup_outer_color()
		self._setup_angle()
		self._setup_type_sections()
		layout.addStretch()

		self._hide_all()

	def _setup_position(self) -> None:
		self._group_pos = QGroupBox("爆炸中心")
		form = QFormLayout(self._group_pos)
		self._spin_pos_x = QDoubleSpinBox()
		self._spin_pos_x.setRange(-100000, 100000)
		self._spin_pos_x.setDecimals(2)
		self._add_row(form, "fw_pos_x", "X:", self._spin_pos_x)
		self._spin_pos_y = QDoubleSpinBox()
		self._spin_pos_y.setRange(-64, 320)
		self._spin_pos_y.setDecimals(2)
		self._add_row(form, "fw_pos_y", "Y:", self._spin_pos_y)
		self._spin_pos_z = QDoubleSpinBox()
		self._spin_pos_z.setRange(-100000, 100000)
		self._spin_pos_z.setDecimals(2)
		self._add_row(form, "fw_pos_z", "Z:", self._spin_pos_z)
		self._spin_pos_x.valueChanged.connect(self._on_pos_changed)
		self._spin_pos_y.valueChanged.connect(self._on_pos_changed)
		self._spin_pos_z.valueChanged.connect(self._on_pos_changed)
		self._btn_pos_select = QPushButton("在地图上选择...")
		self._btn_pos_select.clicked.connect(lambda: self.position_select_requested.emit("firework"))
		form.addRow("", self._btn_pos_select)
		self.layout().addWidget(self._group_pos)

	def _on_pos_changed(self) -> None:
		if self._loading:
			return
		e = self._element
		if e is None:
			return
		pos = Position(x=self._spin_pos_x.value(), y=self._spin_pos_y.value(), z=self._spin_pos_z.value())
		if isinstance(e, TrajFireworkElement):
			e.mid_position = pos
		elif isinstance(e, FireworkElement):
			e.position = pos
		self._emit("position", None)

	def _setup_inner_color(self) -> None:
		self._group_inner = QGroupBox("烟花颜色")
		layout = QVBoxLayout(self._group_inner)
		self._chk_inner_gradient = QCheckBox("使用渐变")
		layout.addWidget(self._chk_inner_gradient)
		self._chk_inner_gradient.toggled.connect(lambda v: self._emit("inner_gradient", v))
		self._color_inner_start = ColorPicker("开始:")
		layout.addWidget(self._color_inner_start)
		self._color_inner_end = ColorPicker("结束:")
		layout.addWidget(self._color_inner_end)
		self._color_inner_start.color_changed.connect(lambda c: self._emit("inner_color_start", ColorRGB(r=c.r, g=c.g, b=c.b)))
		self._color_inner_end.color_changed.connect(lambda c: self._emit("inner_color_end", ColorRGB(r=c.r, g=c.g, b=c.b)))
		self.layout().addWidget(self._group_inner)

	def _setup_outer_color(self) -> None:
		self._group_outer = QGroupBox("外层颜色")
		layout = QVBoxLayout(self._group_outer)
		self._chk_outer_gradient = QCheckBox("使用渐变")
		layout.addWidget(self._chk_outer_gradient)
		self._chk_outer_gradient.toggled.connect(lambda v: self._emit("outer_gradient", v))
		self._color_outer_start = ColorPicker("开始:")
		layout.addWidget(self._color_outer_start)
		self._color_outer_end = ColorPicker("结束:")
		layout.addWidget(self._color_outer_end)
		self._color_outer_start.color_changed.connect(lambda c: self._emit("outer_color_start", ColorRGB(r=c.r, g=c.g, b=c.b)))
		self._color_outer_end.color_changed.connect(lambda c: self._emit("outer_color_end", ColorRGB(r=c.r, g=c.g, b=c.b)))
		self.layout().addWidget(self._group_outer)

	def _setup_angle(self) -> None:
		self._group_angle = QGroupBox("爆炸角度")
		layout = QVBoxLayout(self._group_angle)
		layout.setAlignment(Qt.AlignCenter)

		row = QHBoxLayout()
		row.setAlignment(Qt.AlignCenter)
		row.addStretch()

		h_grp = QVBoxLayout()
		h_grp.setAlignment(Qt.AlignCenter)
		self._dial_h = QDial()
		self._dial_h.setRange(1, 360)
		self._dial_h.setValue(30)
		self._dial_h.setNotchesVisible(True)
		self._dial_h.setFixedSize(80, 80)
		h_grp.addWidget(self._dial_h, alignment=Qt.AlignCenter)
		h_lbl = QLabel("水平角度")
		h_lbl.setAlignment(Qt.AlignCenter)
		h_grp.addWidget(h_lbl)
		self._spin_h_angle = QDoubleSpinBox()
		self._spin_h_angle.setRange(1, 360)
		self._spin_h_angle.setValue(30)
		self._spin_h_angle.setFixedWidth(80)
		self._dial_h.valueChanged.connect(lambda v: self._spin_h_angle.setValue(v))
		self._spin_h_angle.valueChanged.connect(lambda v: self._dial_h.setValue(int(v)))
		h_grp.addWidget(self._spin_h_angle, alignment=Qt.AlignCenter)
		row.addLayout(h_grp)

		row.addSpacing(30)

		v_grp = QVBoxLayout()
		v_grp.setAlignment(Qt.AlignCenter)
		self._dial_v = QDial()
		self._dial_v.setRange(1, 180)
		self._dial_v.setValue(30)
		self._dial_v.setNotchesVisible(True)
		self._dial_v.setFixedSize(80, 80)
		v_grp.addWidget(self._dial_v, alignment=Qt.AlignCenter)
		v_lbl = QLabel("垂直角度")
		v_lbl.setAlignment(Qt.AlignCenter)
		v_grp.addWidget(v_lbl)
		self._spin_v_angle = QDoubleSpinBox()
		self._spin_v_angle.setRange(1, 180)
		self._spin_v_angle.setValue(30)
		self._spin_v_angle.setFixedWidth(80)
		self._dial_v.valueChanged.connect(lambda v: self._spin_v_angle.setValue(v))
		self._spin_v_angle.valueChanged.connect(lambda v: self._dial_v.setValue(int(v)))
		v_grp.addWidget(self._spin_v_angle, alignment=Qt.AlignCenter)
		row.addLayout(v_grp)

		row.addStretch()
		layout.addLayout(row)
		self.layout().addWidget(self._group_angle)

	def _setup_type_sections(self) -> None:
		"""子类重写以添加类型专属参数组."""

	def _hide_all(self) -> None:
		for grp in [self._group_pos, self._group_inner, self._group_outer, self._group_angle]:
			grp.hide()
		for grp in getattr(self, '_sub_groups', []):
			grp.hide()

	def load(self, e: Element, read_only_pos: bool = False) -> None:
		self._loading = True
		self._element = e
		self.block_signals(True)

		self._hide_all()
		self._group_pos.show()
		self._group_inner.show()

		if isinstance(e, TrajFireworkElement):
			mp = e.mid_position
			self._spin_pos_x.setValue(mp.x if mp else 0)
			self._spin_pos_y.setValue(mp.y if mp else 0)
			self._spin_pos_z.setValue(mp.z if mp else 0)
		else:
			self._spin_pos_x.setValue(e.position.x)
			self._spin_pos_y.setValue(e.position.y)
			self._spin_pos_z.setValue(e.position.z)
		self._spin_pos_x.setReadOnly(read_only_pos)
		self._spin_pos_y.setReadOnly(read_only_pos)
		self._spin_pos_z.setReadOnly(read_only_pos)
		self._btn_pos_select.setVisible(not read_only_pos)
		if read_only_pos:
			self._group_pos.setTitle("爆炸中心（由轨迹终点决定）")
		else:
			self._group_pos.setTitle("爆炸中心")

		self._chk_inner_gradient.setChecked(e.inner_color.use_gradient)
		self._color_inner_end.setEnabled(e.inner_color.use_gradient)
		c = e.inner_color.start
		_fw_log.debug(f"load inner_color.start: ColorRGB({c.r},{c.g},{c.b}) type={type(c).__name__}")
		self._color_inner_start.set_color(c)
		c = e.inner_color.end
		self._color_inner_end.set_color(c)

		self._load_type_sections(e)
		self.block_signals(False)
		self._loading = False
		self._update_reset_buttons()

	def _load_type_sections(self, e: Element) -> None:
		"""子类重写以加载类型专属数据."""

	def clear_form(self) -> None:
		self._element = None
		self._hide_all()
		self.hide()

	def _emit(self, key: str, value: object) -> None:
		if self._element is None or self._loading:
			return
		e = self._element
		old_value = getattr(e, key, None)

		if key == "inner_gradient":
			e.inner_color.use_gradient = value
			self._color_inner_end.setEnabled(value)
		elif key == "outer_gradient":
			e.outer_color.use_gradient = value
			self._color_outer_end.setEnabled(value)
		elif key == "inner_color_start":
			old_value = e.inner_color.start
			_fw_log.debug(f"_emit {key}: old=ColorRGB({old_value.r},{old_value.g},{old_value.b}) -> new=ColorRGB({value.r},{value.g},{value.b})")
			e.inner_color.start = value
			_fw_log.debug(f"_emit {key}: after set, elem.inner_color.start=ColorRGB({e.inner_color.start.r},{e.inner_color.start.g},{e.inner_color.start.b})")
		elif key == "inner_color_end":
			old_value = e.inner_color.end
			e.inner_color.end = value
		elif key == "outer_color_start":
			old_value = e.outer_color.start
			e.outer_color.start = value
		elif key == "outer_color_end":
			old_value = e.outer_color.end
			e.outer_color.end = value
		elif key in ("position", "extra"):
			pass

		self.property_changed.emit(e.id, key, value, old_value)
