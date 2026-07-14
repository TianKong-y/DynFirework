# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about.ui'
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
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QSizePolicy, QToolButton, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(768, 560)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Monocraft Nerd Font"])
        font.setPointSize(40)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"padding: 30px;\n"
"color: rgb(26, 95, 180);")
        self.label.setTextFormat(Qt.TextFormat.MarkdownText)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamilies([u"Monocraft Nerd Font"])
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(26, 95, 180);")
        self.label_2.setTextFormat(Qt.TextFormat.MarkdownText)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setFont(font1)
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_17 = QLabel(self.widget)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout.addWidget(self.label_17, 1, 2, 1, 1)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)

        self.label_12 = QLabel(self.widget)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 3, 1, 1, 1)

        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_7, 5, 1, 1, 1)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_5, 6, 1, 1, 1)

        self.label_14 = QLabel(self.widget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_14, 10, 1, 1, 1)

        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setTextFormat(Qt.TextFormat.MarkdownText)

        self.verticalLayout_2.addWidget(self.label_6)

        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setTextFormat(Qt.TextFormat.MarkdownText)

        self.verticalLayout_2.addWidget(self.label_9)


        self.gridLayout.addWidget(self.frame, 6, 2, 1, 1)

        self.label_13 = QLabel(self.widget)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout.addWidget(self.label_13, 3, 2, 1, 1)

        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        sizePolicy1.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.label_8, 5, 2, 1, 1)

        self.label_15 = QLabel(self.widget)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout.addWidget(self.label_15, 10, 2, 1, 1)

        self.label_16 = QLabel(self.widget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_16, 1, 1, 1, 1)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1)

        self.label_10 = QLabel(self.widget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_10, 2, 1, 1, 1)

        self.label_11 = QLabel(self.widget)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 2, 2, 1, 1)


        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(Dialog)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.dynfirework_github_toolbutton = QToolButton(self.widget_2)
        self.dynfirework_github_toolbutton.setObjectName(u"dynfirework_github_toolbutton")
        font2 = QFont()
        font2.setPointSize(48)
        self.dynfirework_github_toolbutton.setFont(font2)
        self.dynfirework_github_toolbutton.setStyleSheet(u"background: transparent;\n"
"color: rgb(26, 95, 180);\n"
"border: none;\n"
"")
        self.dynfirework_github_toolbutton.setIconSize(QSize(64, 64))

        self.horizontalLayout_2.addWidget(self.dynfirework_github_toolbutton)

        self.dfmod_toolbutton = QToolButton(self.widget_2)
        self.dfmod_toolbutton.setObjectName(u"dfmod_toolbutton")
        self.dfmod_toolbutton.setFont(font2)
        self.dfmod_toolbutton.setStyleSheet(u"background: transparent;\n"
"color: rgb(198, 70, 0);\n"
"border: none;\n"
"")
        self.dfmod_toolbutton.setIconSize(QSize(64, 64))

        self.horizontalLayout_2.addWidget(self.dfmod_toolbutton)

        self.issue_toolbutton = QToolButton(self.widget_2)
        self.issue_toolbutton.setObjectName(u"issue_toolbutton")
        font3 = QFont()
        font3.setPointSize(40)
        self.issue_toolbutton.setFont(font3)
        self.issue_toolbutton.setStyleSheet(u"background: transparent;\n"
"color: #57ab5a;\n"
"border: none;\n"
"")
        self.issue_toolbutton.setIconSize(QSize(64, 64))

        self.horizontalLayout_2.addWidget(self.issue_toolbutton)

        self.contribute_toolbutton = QToolButton(self.widget_2)
        self.contribute_toolbutton.setObjectName(u"contribute_toolbutton")
        self.contribute_toolbutton.setFont(font2)
        self.contribute_toolbutton.setStyleSheet(u"background: transparent;\n"
"color: #986ee2;\n"
"border: none;\n"
"")
        self.contribute_toolbutton.setIconSize(QSize(64, 64))

        self.horizontalLayout_2.addWidget(self.contribute_toolbutton)

        self.pyside_toolbutton = QToolButton(self.widget_2)
        self.pyside_toolbutton.setObjectName(u"pyside_toolbutton")
        self.pyside_toolbutton.setFont(font2)
        self.pyside_toolbutton.setStyleSheet(u"background: transparent;\n"
"color: #41cd52;\n"
"border: none;")
        self.pyside_toolbutton.setIconSize(QSize(64, 64))

        self.horizontalLayout_2.addWidget(self.pyside_toolbutton)

        self.python_toolbutton = QToolButton(self.widget_2)
        self.python_toolbutton.setObjectName(u"python_toolbutton")
        self.python_toolbutton.setFont(font2)
        self.python_toolbutton.setStyleSheet(u"background: transparent;\n"
"color: rgb(245, 194, 17);\n"
"border: none;")
        self.python_toolbutton.setIconSize(QSize(64, 64))

        self.horizontalLayout_2.addWidget(self.python_toolbutton)

        self.minecraft_toolbutton = QToolButton(self.widget_2)
        self.minecraft_toolbutton.setObjectName(u"minecraft_toolbutton")
        self.minecraft_toolbutton.setFont(font2)
        self.minecraft_toolbutton.setStyleSheet(u"background: transparent;\n"
"color:#52a535;\n"
"border: none;")
        self.minecraft_toolbutton.setIconSize(QSize(64, 64))

        self.horizontalLayout_2.addWidget(self.minecraft_toolbutton)


        self.verticalLayout.addWidget(self.widget_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        font4 = QFont()
        font4.setFamilies([u"Ark Pixel 12px P zh_cn"])
        self.buttonBox.setFont(font4)
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
        self.label.setText(QCoreApplication.translate("Dialog", u"**DynFirework**", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Powered By **PySide6**", None))
        self.label_17.setText(QCoreApplication.translate("Dialog", u"Qt 6.11.1", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Version:", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"Template Contributors:", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"BackEnd Contributors:", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"BackEnd Version:", None))
        self.label_14.setText(QCoreApplication.translate("Dialog", u"License:", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"[DynFirework Mod: v2.0](https://github.com/TianKong-y/DynFireworkMod)", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"[ColorBlock Mod: BiliBili](www.bilibili.com/list/ml1854134356?oid=606725579&bvid=BV1984y1s79M)", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"TianKong-y", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"TianKong-y, MCXCC303", None))
        self.label_15.setText(QCoreApplication.translate("Dialog", u"GPL-3.0", None))
        self.label_16.setText(QCoreApplication.translate("Dialog", u"Qt Version:", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"<DYNFIREWORK_VERSION>", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"GUI Contributors:", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"MCXCC303", None))
#if QT_CONFIG(tooltip)
        self.dynfirework_github_toolbutton.setToolTip(QCoreApplication.translate("Dialog", u"DynFirework - Github", None))
#endif // QT_CONFIG(tooltip)
        self.dynfirework_github_toolbutton.setText(QCoreApplication.translate("Dialog", u"\uf09b", None))
#if QT_CONFIG(tooltip)
        self.dfmod_toolbutton.setToolTip(QCoreApplication.translate("Dialog", u"DynFirework Mod - Github", None))
#endif // QT_CONFIG(tooltip)
        self.dfmod_toolbutton.setText(QCoreApplication.translate("Dialog", u"\uf09b", None))
#if QT_CONFIG(tooltip)
        self.issue_toolbutton.setToolTip(QCoreApplication.translate("Dialog", u"Make issues to DynFirework", None))
#endif // QT_CONFIG(tooltip)
        self.issue_toolbutton.setText(QCoreApplication.translate("Dialog", u"\uf41b", None))
#if QT_CONFIG(tooltip)
        self.contribute_toolbutton.setToolTip(QCoreApplication.translate("Dialog", u"Contribute to DynFirework", None))
#endif // QT_CONFIG(tooltip)
        self.contribute_toolbutton.setText(QCoreApplication.translate("Dialog", u"\uf419", None))
#if QT_CONFIG(tooltip)
        self.pyside_toolbutton.setToolTip(QCoreApplication.translate("Dialog", u"Qt for Python - Pyside6", None))
#endif // QT_CONFIG(tooltip)
        self.pyside_toolbutton.setText(QCoreApplication.translate("Dialog", u"\uf375", None))
#if QT_CONFIG(tooltip)
        self.python_toolbutton.setToolTip(QCoreApplication.translate("Dialog", u"Python 3.10+", None))
#endif // QT_CONFIG(tooltip)
        self.python_toolbutton.setText(QCoreApplication.translate("Dialog", u"\ued1b", None))
#if QT_CONFIG(tooltip)
        self.minecraft_toolbutton.setToolTip(QCoreApplication.translate("Dialog", u"Minecraft", None))
#endif // QT_CONFIG(tooltip)
        self.minecraft_toolbutton.setText(QCoreApplication.translate("Dialog", u"\U000f0373", None))
    # retranslateUi

