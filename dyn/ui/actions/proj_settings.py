# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'proj_settings.ui'
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
    QHBoxLayout, QLabel, QLineEdit, QSizePolicy,
    QSpacerItem, QSpinBox, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(553, 412)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.proj_settings = QLabel(Dialog)
        self.proj_settings.setObjectName(u"proj_settings")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.proj_settings.sizePolicy().hasHeightForWidth())
        self.proj_settings.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Ark Pixel 12px P zh_cn"])
        font.setPointSize(20)
        font.setBold(False)
        self.proj_settings.setFont(font)
        self.proj_settings.setTextFormat(Qt.TextFormat.MarkdownText)
        self.proj_settings.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.proj_settings)

        self.full_widget = QWidget(Dialog)
        self.full_widget.setObjectName(u"full_widget")
        font1 = QFont()
        font1.setFamilies([u"Ark Pixel 12px P zh_cn"])
        self.full_widget.setFont(font1)
        self.gridLayout = QGridLayout(self.full_widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.namespace_edit = QLineEdit(self.full_widget)
        self.namespace_edit.setObjectName(u"namespace_edit")
        font2 = QFont()
        font2.setFamilies([u"Ubuntu"])
        self.namespace_edit.setFont(font2)

        self.gridLayout.addWidget(self.namespace_edit, 4, 1, 1, 1)

        self.time_signature = QLabel(self.full_widget)
        self.time_signature.setObjectName(u"time_signature")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.time_signature.sizePolicy().hasHeightForWidth())
        self.time_signature.setSizePolicy(sizePolicy1)
        self.time_signature.setFont(font1)
        self.time_signature.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.time_signature, 7, 0, 1, 1)

        self.namespace_label = QLabel(self.full_widget)
        self.namespace_label.setObjectName(u"namespace_label")
        sizePolicy1.setHeightForWidth(self.namespace_label.sizePolicy().hasHeightForWidth())
        self.namespace_label.setSizePolicy(sizePolicy1)
        self.namespace_label.setFont(font1)
        self.namespace_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.namespace_label, 4, 0, 1, 1)

        self.proj_name_edit = QLineEdit(self.full_widget)
        self.proj_name_edit.setObjectName(u"proj_name_edit")
        self.proj_name_edit.setFont(font2)

        self.gridLayout.addWidget(self.proj_name_edit, 3, 1, 1, 1)

        self.backend_text = QLabel(self.full_widget)
        self.backend_text.setObjectName(u"backend_text")
        sizePolicy.setHeightForWidth(self.backend_text.sizePolicy().hasHeightForWidth())
        self.backend_text.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setFamilies([u"Monocraft Nerd Font"])
        self.backend_text.setFont(font3)

        self.gridLayout.addWidget(self.backend_text, 0, 1, 1, 1)

        self.bpm_spinbox = QDoubleSpinBox(self.full_widget)
        self.bpm_spinbox.setObjectName(u"bpm_spinbox")
        self.bpm_spinbox.setFont(font2)
        self.bpm_spinbox.setMinimum(1.000000000000000)
        self.bpm_spinbox.setMaximum(999.000000000000000)
        self.bpm_spinbox.setValue(120.000000000000000)

        self.gridLayout.addWidget(self.bpm_spinbox, 6, 1, 1, 1)

        self.line = QFrame(self.full_widget)
        self.line.setObjectName(u"line")
        self.line.setFont(font1)
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line, 2, 0, 1, 2)

        self.audio_offset = QLabel(self.full_widget)
        self.audio_offset.setObjectName(u"audio_offset")
        sizePolicy1.setHeightForWidth(self.audio_offset.sizePolicy().hasHeightForWidth())
        self.audio_offset.setSizePolicy(sizePolicy1)
        self.audio_offset.setFont(font1)
        self.audio_offset.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.audio_offset, 8, 0, 1, 1)

        self.proj_name = QLabel(self.full_widget)
        self.proj_name.setObjectName(u"proj_name")
        sizePolicy1.setHeightForWidth(self.proj_name.sizePolicy().hasHeightForWidth())
        self.proj_name.setSizePolicy(sizePolicy1)
        self.proj_name.setFont(font1)
        self.proj_name.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.proj_name, 3, 0, 1, 1)

        self.backend = QLabel(self.full_widget)
        self.backend.setObjectName(u"backend")
        sizePolicy1.setHeightForWidth(self.backend.sizePolicy().hasHeightForWidth())
        self.backend.setSizePolicy(sizePolicy1)
        self.backend.setFont(font1)
        self.backend.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.backend, 0, 0, 1, 1)

        self.audio_offset_spinbox = QSpinBox(self.full_widget)
        self.audio_offset_spinbox.setObjectName(u"audio_offset_spinbox")
        self.audio_offset_spinbox.setFont(font2)
        self.audio_offset_spinbox.setMinimum(-999)
        self.audio_offset_spinbox.setMaximum(999)

        self.gridLayout.addWidget(self.audio_offset_spinbox, 8, 1, 1, 1)

        self.bpm = QLabel(self.full_widget)
        self.bpm.setObjectName(u"bpm")
        sizePolicy1.setHeightForWidth(self.bpm.sizePolicy().hasHeightForWidth())
        self.bpm.setSizePolicy(sizePolicy1)
        self.bpm.setFont(font1)
        self.bpm.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.bpm, 6, 0, 1, 1)

        self.mc_version = QLabel(self.full_widget)
        self.mc_version.setObjectName(u"mc_version")
        sizePolicy1.setHeightForWidth(self.mc_version.sizePolicy().hasHeightForWidth())
        self.mc_version.setSizePolicy(sizePolicy1)
        self.mc_version.setFont(font1)
        self.mc_version.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.mc_version, 1, 0, 1, 1)

        self.mc_version_box = QComboBox(self.full_widget)
        self.mc_version_box.setObjectName(u"mc_version_box")
        self.mc_version_box.setFont(font2)

        self.gridLayout.addWidget(self.mc_version_box, 1, 1, 1, 1)

        self.time_signature_widget = QWidget(self.full_widget)
        self.time_signature_widget.setObjectName(u"time_signature_widget")
        sizePolicy.setHeightForWidth(self.time_signature_widget.sizePolicy().hasHeightForWidth())
        self.time_signature_widget.setSizePolicy(sizePolicy)
        self.time_signature_widget.setFont(font1)
        self.horizontalLayout = QHBoxLayout(self.time_signature_widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.time_signature_1 = QSpinBox(self.time_signature_widget)
        self.time_signature_1.setObjectName(u"time_signature_1")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.time_signature_1.sizePolicy().hasHeightForWidth())
        self.time_signature_1.setSizePolicy(sizePolicy2)
        self.time_signature_1.setFont(font2)
        self.time_signature_1.setMinimum(1)
        self.time_signature_1.setMaximum(99)
        self.time_signature_1.setValue(4)

        self.horizontalLayout.addWidget(self.time_signature_1)

        self.time_signature_split = QLabel(self.time_signature_widget)
        self.time_signature_split.setObjectName(u"time_signature_split")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.time_signature_split.sizePolicy().hasHeightForWidth())
        self.time_signature_split.setSizePolicy(sizePolicy3)
        self.time_signature_split.setFont(font1)
        self.time_signature_split.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.time_signature_split)

        self.time_signature_2 = QSpinBox(self.time_signature_widget)
        self.time_signature_2.setObjectName(u"time_signature_2")
        sizePolicy2.setHeightForWidth(self.time_signature_2.sizePolicy().hasHeightForWidth())
        self.time_signature_2.setSizePolicy(sizePolicy2)
        self.time_signature_2.setFont(font2)
        self.time_signature_2.setMinimum(1)
        self.time_signature_2.setValue(4)

        self.horizontalLayout.addWidget(self.time_signature_2)

        self.horizontalSpacer = QSpacerItem(488, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.gridLayout.addWidget(self.time_signature_widget, 7, 1, 1, 1)

        self.namespace_strict = QLabel(self.full_widget)
        self.namespace_strict.setObjectName(u"namespace_strict")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.namespace_strict.sizePolicy().hasHeightForWidth())
        self.namespace_strict.setSizePolicy(sizePolicy4)
        font4 = QFont()
        font4.setFamilies([u"Ark Pixel 12px P zh_cn"])
        font4.setPointSize(9)
        font4.setItalic(False)
        self.namespace_strict.setFont(font4)

        self.gridLayout.addWidget(self.namespace_strict, 5, 1, 1, 1)


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
        self.proj_settings.setText(QCoreApplication.translate("Dialog", u"**\u9879\u76ee\u8bbe\u7f6e**", None))
        self.namespace_edit.setText(QCoreApplication.translate("Dialog", u"untitled1", None))
        self.time_signature.setText(QCoreApplication.translate("Dialog", u"\u62cd\u53f7\uff1a", None))
        self.namespace_label.setText(QCoreApplication.translate("Dialog", u"\u547d\u540d\u7a7a\u95f4\uff1a", None))
        self.proj_name_edit.setText(QCoreApplication.translate("Dialog", u"Untitled", None))
        self.backend_text.setText(QCoreApplication.translate("Dialog", u"<\u9009\u5b9a\u6a21\u7ec4\u540e\u7aef>", None))
        self.audio_offset.setText(QCoreApplication.translate("Dialog", u"\u97f3\u9891\u504f\u79fb\uff1a", None))
        self.proj_name.setText(QCoreApplication.translate("Dialog", u"\u9879\u76ee\u540d\u79f0\uff1a", None))
        self.backend.setText(QCoreApplication.translate("Dialog", u"\u6a21\u7ec4\u540e\u7aef\uff1a", None))
        self.audio_offset_spinbox.setSuffix(QCoreApplication.translate("Dialog", u" ms", None))
        self.bpm.setText(QCoreApplication.translate("Dialog", u"BPM\uff1a", None))
        self.mc_version.setText(QCoreApplication.translate("Dialog", u"Minecraft\u7248\u672c\uff1a", None))
        self.time_signature_split.setText(QCoreApplication.translate("Dialog", u"/", None))
        self.namespace_strict.setText(QCoreApplication.translate("Dialog", u"\u4ec5\u9650\u5c0f\u5199\u5b57\u6bcd\u3001\u6570\u5b57\u3001\u4e0b\u5212\u7ebf\u548c\u70b9", None))
    # retranslateUi

