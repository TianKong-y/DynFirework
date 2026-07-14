# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_proj_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QDoubleSpinBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(638, 445)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.create_new_proj = QLabel(Dialog)
        self.create_new_proj.setObjectName(u"create_new_proj")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.create_new_proj.sizePolicy().hasHeightForWidth())
        self.create_new_proj.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Ark Pixel 12px P zh_cn"])
        font.setPointSize(20)
        font.setBold(False)
        self.create_new_proj.setFont(font)
        self.create_new_proj.setTextFormat(Qt.TextFormat.MarkdownText)
        self.create_new_proj.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.create_new_proj)

        self.full_widget = QWidget(Dialog)
        self.full_widget.setObjectName(u"full_widget")
        self.gridLayout = QGridLayout(self.full_widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.widget = QWidget(self.full_widget)
        self.widget.setObjectName(u"widget")
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.time_signature_1 = QSpinBox(self.widget)
        self.time_signature_1.setObjectName(u"time_signature_1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.time_signature_1.sizePolicy().hasHeightForWidth())
        self.time_signature_1.setSizePolicy(sizePolicy1)
        self.time_signature_1.setMinimum(1)
        self.time_signature_1.setMaximum(99)
        self.time_signature_1.setValue(4)

        self.horizontalLayout.addWidget(self.time_signature_1)

        self.time_signature_split = QLabel(self.widget)
        self.time_signature_split.setObjectName(u"time_signature_split")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.time_signature_split.sizePolicy().hasHeightForWidth())
        self.time_signature_split.setSizePolicy(sizePolicy2)
        self.time_signature_split.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.time_signature_split)

        self.time_signature_2 = QSpinBox(self.widget)
        self.time_signature_2.setObjectName(u"time_signature_2")
        sizePolicy1.setHeightForWidth(self.time_signature_2.sizePolicy().hasHeightForWidth())
        self.time_signature_2.setSizePolicy(sizePolicy1)
        self.time_signature_2.setMinimum(1)
        self.time_signature_2.setValue(4)

        self.horizontalLayout.addWidget(self.time_signature_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.gridLayout.addWidget(self.widget, 8, 1, 1, 1)

        self.mc_version_box = QComboBox(self.full_widget)
        self.mc_version_box.setObjectName(u"mc_version_box")

        self.gridLayout.addWidget(self.mc_version_box, 1, 1, 1, 1)

        self.line = QFrame(self.full_widget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line, 2, 0, 1, 2)

        self.proj_name = QLabel(self.full_widget)
        self.proj_name.setObjectName(u"proj_name")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.proj_name.sizePolicy().hasHeightForWidth())
        self.proj_name.setSizePolicy(sizePolicy3)
        font1 = QFont()
        font1.setFamilies([u"Ark Pixel 12px P zh_cn"])
        self.proj_name.setFont(font1)
        self.proj_name.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.proj_name, 4, 0, 1, 1)

        self.bpm_spinbox = QDoubleSpinBox(self.full_widget)
        self.bpm_spinbox.setObjectName(u"bpm_spinbox")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.bpm_spinbox.sizePolicy().hasHeightForWidth())
        self.bpm_spinbox.setSizePolicy(sizePolicy4)
        self.bpm_spinbox.setMinimum(1.000000000000000)
        self.bpm_spinbox.setMaximum(999.000000000000000)
        self.bpm_spinbox.setValue(120.000000000000000)

        self.gridLayout.addWidget(self.bpm_spinbox, 7, 1, 1, 1)

        self.editables = QLabel(self.full_widget)
        self.editables.setObjectName(u"editables")
        sizePolicy.setHeightForWidth(self.editables.sizePolicy().hasHeightForWidth())
        self.editables.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamilies([u"Ark Pixel 12px P zh_cn"])
        font2.setPointSize(9)
        font2.setItalic(False)
        self.editables.setFont(font2)
        self.editables.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.editables, 3, 0, 1, 2)

        self.time_signature = QLabel(self.full_widget)
        self.time_signature.setObjectName(u"time_signature")
        sizePolicy3.setHeightForWidth(self.time_signature.sizePolicy().hasHeightForWidth())
        self.time_signature.setSizePolicy(sizePolicy3)
        self.time_signature.setFont(font1)
        self.time_signature.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.time_signature, 8, 0, 1, 1)

        self.backend_box = QComboBox(self.full_widget)
        self.backend_box.addItem("")
        self.backend_box.addItem("")
        self.backend_box.setObjectName(u"backend_box")

        self.gridLayout.addWidget(self.backend_box, 0, 1, 1, 1)

        self.bpm = QLabel(self.full_widget)
        self.bpm.setObjectName(u"bpm")
        sizePolicy3.setHeightForWidth(self.bpm.sizePolicy().hasHeightForWidth())
        self.bpm.setSizePolicy(sizePolicy3)
        self.bpm.setFont(font1)
        self.bpm.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.bpm, 7, 0, 1, 1)

        self.namespace_edit = QLineEdit(self.full_widget)
        self.namespace_edit.setObjectName(u"namespace_edit")

        self.gridLayout.addWidget(self.namespace_edit, 5, 1, 1, 1)

        self.proj_name_edit = QLineEdit(self.full_widget)
        self.proj_name_edit.setObjectName(u"proj_name_edit")

        self.gridLayout.addWidget(self.proj_name_edit, 4, 1, 1, 1)

        self.backend = QLabel(self.full_widget)
        self.backend.setObjectName(u"backend")
        sizePolicy3.setHeightForWidth(self.backend.sizePolicy().hasHeightForWidth())
        self.backend.setSizePolicy(sizePolicy3)
        self.backend.setFont(font1)
        self.backend.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.backend, 0, 0, 1, 1)

        self.namespace_label = QLabel(self.full_widget)
        self.namespace_label.setObjectName(u"namespace_label")
        sizePolicy3.setHeightForWidth(self.namespace_label.sizePolicy().hasHeightForWidth())
        self.namespace_label.setSizePolicy(sizePolicy3)
        self.namespace_label.setFont(font1)
        self.namespace_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.namespace_label, 5, 0, 1, 1)

        self.audio_offset_spinbox = QSpinBox(self.full_widget)
        self.audio_offset_spinbox.setObjectName(u"audio_offset_spinbox")
        self.audio_offset_spinbox.setMinimum(-999)
        self.audio_offset_spinbox.setMaximum(999)

        self.gridLayout.addWidget(self.audio_offset_spinbox, 9, 1, 1, 1)

        self.mc_version = QLabel(self.full_widget)
        self.mc_version.setObjectName(u"mc_version")
        sizePolicy3.setHeightForWidth(self.mc_version.sizePolicy().hasHeightForWidth())
        self.mc_version.setSizePolicy(sizePolicy3)
        self.mc_version.setFont(font1)
        self.mc_version.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.mc_version, 1, 0, 1, 1)

        self.audio_offset = QLabel(self.full_widget)
        self.audio_offset.setObjectName(u"audio_offset")
        sizePolicy3.setHeightForWidth(self.audio_offset.sizePolicy().hasHeightForWidth())
        self.audio_offset.setSizePolicy(sizePolicy3)
        self.audio_offset.setFont(font1)
        self.audio_offset.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.audio_offset, 9, 0, 1, 1)

        self.namespace_strict = QLabel(self.full_widget)
        self.namespace_strict.setObjectName(u"namespace_strict")
        sizePolicy.setHeightForWidth(self.namespace_strict.sizePolicy().hasHeightForWidth())
        self.namespace_strict.setSizePolicy(sizePolicy)
        self.namespace_strict.setFont(font2)

        self.gridLayout.addWidget(self.namespace_strict, 6, 1, 1, 1)


        self.verticalLayout.addWidget(self.full_widget)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setFont(font1)
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.create_new_proj.setText(QCoreApplication.translate("Dialog", u"**\u521b\u5efa\u65b0\u7684\u9879\u76ee**", None))
        self.time_signature_split.setText(QCoreApplication.translate("Dialog", u"/", None))
        self.mc_version_box.setCurrentText("")
        self.proj_name.setText(QCoreApplication.translate("Dialog", u"\u9879\u76ee\u540d\u79f0\uff1a", None))
        self.editables.setText(QCoreApplication.translate("Dialog", u"\u4f60\u53ef\u4ee5\u5728\u9879\u76ee\u521b\u5efa\u540e\u66f4\u6539\u4ee5\u4e0b\u6761\u76ee\u7684\u503c\u3002", None))
        self.time_signature.setText(QCoreApplication.translate("Dialog", u"\u62cd\u53f7\uff1a", None))
        self.backend_box.setItemText(0, QCoreApplication.translate("Dialog", u"DynFireworkMod v2.0 (/df)", None))
        self.backend_box.setItemText(1, QCoreApplication.translate("Dialog", u"ColorBlock (/particleex)", None))

        self.bpm.setText(QCoreApplication.translate("Dialog", u"BPM\uff1a", None))
        self.namespace_edit.setText(QCoreApplication.translate("Dialog", u"untitled1", None))
        self.proj_name_edit.setText(QCoreApplication.translate("Dialog", u"Untitled", None))
        self.backend.setText(QCoreApplication.translate("Dialog", u"\u6a21\u7ec4\u540e\u7aef\uff1a", None))
        self.namespace_label.setText(QCoreApplication.translate("Dialog", u"\u547d\u540d\u7a7a\u95f4\uff1a", None))
        self.audio_offset_spinbox.setSuffix(QCoreApplication.translate("Dialog", u" ms", None))
        self.mc_version.setText(QCoreApplication.translate("Dialog", u"Minecraft\u7248\u672c\uff1a", None))
        self.audio_offset.setText(QCoreApplication.translate("Dialog", u"\u97f3\u9891\u504f\u79fb\uff1a", None))
        self.namespace_strict.setText(QCoreApplication.translate("Dialog", u"\u4ec5\u9650\u5c0f\u5199\u5b57\u6bcd\u3001\u6570\u5b57\u3001\u4e0b\u5212\u7ebf\u548c\u70b9", None))
    # retranslateUi

