# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'export_as_datapack_dialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFrame, QGridLayout, QLabel, QLayout,
    QLineEdit, QSizePolicy, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(662, 513)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.export_to_datapack = QLabel(Dialog)
        self.export_to_datapack.setObjectName(u"export_to_datapack")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.export_to_datapack.sizePolicy().hasHeightForWidth())
        self.export_to_datapack.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Ark Pixel 12px P zh_cn"])
        font.setPointSize(20)
        font.setBold(False)
        self.export_to_datapack.setFont(font)
        self.export_to_datapack.setTextFormat(Qt.TextFormat.MarkdownText)
        self.export_to_datapack.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.export_to_datapack)

        self.full_widget = QWidget(Dialog)
        self.full_widget.setObjectName(u"full_widget")
        font1 = QFont()
        font1.setFamilies([u"Ark Pixel 12px P zh_cn"])
        self.full_widget.setFont(font1)
        self.gridLayout = QGridLayout(self.full_widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.pack_format_number = QLabel(self.full_widget)
        self.pack_format_number.setObjectName(u"pack_format_number")
        self.pack_format_number.setFont(font1)

        self.gridLayout.addWidget(self.pack_format_number, 6, 1, 1, 1)

        self.unchangeable = QLabel(self.full_widget)
        self.unchangeable.setObjectName(u"unchangeable")
        font2 = QFont()
        font2.setFamilies([u"Ark Pixel 12px P zh_cn"])
        font2.setPointSize(9)
        font2.setItalic(False)
        self.unchangeable.setFont(font2)
        self.unchangeable.setTextFormat(Qt.TextFormat.MarkdownText)

        self.gridLayout.addWidget(self.unchangeable, 7, 1, 1, 1)

        self.namespace_strict = QLabel(self.full_widget)
        self.namespace_strict.setObjectName(u"namespace_strict")
        sizePolicy.setHeightForWidth(self.namespace_strict.sizePolicy().hasHeightForWidth())
        self.namespace_strict.setSizePolicy(sizePolicy)
        self.namespace_strict.setFont(font2)
        self.namespace_strict.setTextFormat(Qt.TextFormat.MarkdownText)

        self.gridLayout.addWidget(self.namespace_strict, 2, 1, 1, 1)

        self.datapack_name_edit = QLineEdit(self.full_widget)
        self.datapack_name_edit.setObjectName(u"datapack_name_edit")
        font3 = QFont()
        font3.setFamilies([u"Ubuntu"])
        self.datapack_name_edit.setFont(font3)

        self.gridLayout.addWidget(self.datapack_name_edit, 0, 1, 1, 1)

        self.datapack_name = QLabel(self.full_widget)
        self.datapack_name.setObjectName(u"datapack_name")
        self.datapack_name.setFont(font1)
        self.datapack_name.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.datapack_name, 0, 0, 1, 1)

        self.desc = QLabel(self.full_widget)
        self.desc.setObjectName(u"desc")
        self.desc.setFont(font1)
        self.desc.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop|Qt.AlignmentFlag.AlignTrailing)

        self.gridLayout.addWidget(self.desc, 3, 0, 1, 1)

        self.textEdit = QTextEdit(self.full_widget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setFont(font3)
        self.textEdit.setOverwriteMode(False)

        self.gridLayout.addWidget(self.textEdit, 3, 1, 1, 1)

        self.namespace_label = QLabel(self.full_widget)
        self.namespace_label.setObjectName(u"namespace_label")
        self.namespace_label.setFont(font1)
        self.namespace_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.namespace_label, 1, 0, 1, 1)

        self.namespace_edit = QLineEdit(self.full_widget)
        self.namespace_edit.setObjectName(u"namespace_edit")
        self.namespace_edit.setFont(font3)

        self.gridLayout.addWidget(self.namespace_edit, 1, 1, 1, 1)

        self.mc_version = QLabel(self.full_widget)
        self.mc_version.setObjectName(u"mc_version")
        self.mc_version.setFont(font1)
        self.mc_version.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.mc_version, 5, 0, 1, 1)

        self.mc_version_text = QLabel(self.full_widget)
        self.mc_version_text.setObjectName(u"mc_version_text")
        self.mc_version_text.setFont(font1)

        self.gridLayout.addWidget(self.mc_version_text, 5, 1, 1, 1)

        self.pack_format = QLabel(self.full_widget)
        self.pack_format.setObjectName(u"pack_format")
        self.pack_format.setFont(font1)
        self.pack_format.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.pack_format, 6, 0, 1, 1)

        self.line = QFrame(self.full_widget)
        self.line.setObjectName(u"line")
        self.line.setFont(font1)
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line, 4, 0, 1, 2)


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
        self.export_to_datapack.setText(QCoreApplication.translate("Dialog", u"**\u5bfc\u51fa\u5230\u6570\u636e\u5305**", None))
        self.pack_format_number.setText(QCoreApplication.translate("Dialog", u"<PACK-FORMAT-NUMBER>", None))
        self.unchangeable.setText(QCoreApplication.translate("Dialog", u"\u5982\u9700\u66f4\u6539\uff0c\u8bf7\u8fdb\u5165\u201c\u9879\u76ee\u7ba1\u7406\u201d\u4e2d\u66f4\u6539\u540e\u5bfc\u51fa", None))
        self.namespace_strict.setText(QCoreApplication.translate("Dialog", u"\u4ec5\u9650\u5c0f\u5199\u5b57\u6bcd\u3001\u6570\u5b57\u3001\u4e0b\u5212\u7ebf\u548c\u70b9\uff0c\u7559\u7a7a\u4f7f\u7528\u9879\u76ee\u8bbe\u7f6e", None))
        self.datapack_name_edit.setText(QCoreApplication.translate("Dialog", u"Untitled", None))
        self.datapack_name.setText(QCoreApplication.translate("Dialog", u"\u6570\u636e\u5305\u540d\u79f0\uff1a", None))
        self.desc.setText(QCoreApplication.translate("Dialog", u"\u63cf\u8ff0\uff1a", None))
        self.textEdit.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:14pt; font-weight:300; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"DynFirework datapack", None))
        self.namespace_label.setText(QCoreApplication.translate("Dialog", u"\u547d\u540d\u7a7a\u95f4\uff1a", None))
        self.namespace_edit.setText("")
        self.namespace_edit.setPlaceholderText(QCoreApplication.translate("Dialog", u"untitled1", None))
        self.mc_version.setText(QCoreApplication.translate("Dialog", u"Minecraft\u7248\u672c\uff1a", None))
        self.mc_version_text.setText(QCoreApplication.translate("Dialog", u"MC <VERSION+FORGE/FABRIC>", None))
        self.pack_format.setText(QCoreApplication.translate("Dialog", u"Pack Format\uff1a", None))
    # retranslateUi

