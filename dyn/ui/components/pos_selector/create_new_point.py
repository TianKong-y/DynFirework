# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_new_point.ui'
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
    QDoubleSpinBox, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpinBox, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(578, 487)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        font = QFont()
        font.setFamilies([u"Ark Pixel 12px P zh_cn"])
        self.frame.setFont(font)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lineEdit_Name = QLineEdit(self.frame)
        self.lineEdit_Name.setObjectName(u"lineEdit_Name")
        font1 = QFont()
        font1.setFamilies([u"Ubuntu"])
        self.lineEdit_Name.setFont(font1)

        self.gridLayout_2.addWidget(self.lineEdit_Name, 1, 1, 1, 1)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamilies([u"Ark Pixel 12px P zh_cn"])
        font2.setPointSize(24)
        self.label_4.setFont(font2)
        self.label_4.setTextFormat(Qt.TextFormat.MarkdownText)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 2)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)

        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_4 = QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)

        self.doubleSpinBox_X = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_X.setObjectName(u"doubleSpinBox_X")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.doubleSpinBox_X.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_X.setSizePolicy(sizePolicy2)
        self.doubleSpinBox_X.setFont(font1)
        self.doubleSpinBox_X.setMinimum(-200.000000000000000)
        self.doubleSpinBox_X.setMaximum(200.000000000000000)

        self.gridLayout_4.addWidget(self.doubleSpinBox_X, 0, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_2, 1, 0, 1, 1)

        self.doubleSpinBox_Y = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_Y.setObjectName(u"doubleSpinBox_Y")
        sizePolicy2.setHeightForWidth(self.doubleSpinBox_Y.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_Y.setSizePolicy(sizePolicy2)
        self.doubleSpinBox_Y.setFont(font1)
        self.doubleSpinBox_Y.setMaximum(320.000000000000000)
        self.doubleSpinBox_Y.setValue(80.000000000000000)

        self.gridLayout_4.addWidget(self.doubleSpinBox_Y, 1, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_3, 2, 0, 1, 1)

        self.doubleSpinBox_Z = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_Z.setObjectName(u"doubleSpinBox_Z")
        sizePolicy2.setHeightForWidth(self.doubleSpinBox_Z.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_Z.setSizePolicy(sizePolicy2)
        self.doubleSpinBox_Z.setFont(font1)
        self.doubleSpinBox_Z.setMinimum(-200.000000000000000)
        self.doubleSpinBox_Z.setMaximum(200.000000000000000)

        self.gridLayout_4.addWidget(self.doubleSpinBox_Z, 2, 1, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox, 2, 0, 1, 2)

        self.groupBox_2 = QGroupBox(self.frame)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy3)
        self.groupBox_2.setFont(font)
        self.gridLayout_3 = QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.widget = QWidget(self.groupBox_2)
        self.widget.setObjectName(u"widget")
        self.widget.setFont(font)
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_color_red = QPushButton(self.widget)
        self.pushButton_color_red.setObjectName(u"pushButton_color_red")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.pushButton_color_red.sizePolicy().hasHeightForWidth())
        self.pushButton_color_red.setSizePolicy(sizePolicy4)
        self.pushButton_color_red.setFont(font)
        self.pushButton_color_red.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
"                                                            ")

        self.horizontalLayout.addWidget(self.pushButton_color_red)

        self.pushButton_color_green = QPushButton(self.widget)
        self.pushButton_color_green.setObjectName(u"pushButton_color_green")
        sizePolicy4.setHeightForWidth(self.pushButton_color_green.sizePolicy().hasHeightForWidth())
        self.pushButton_color_green.setSizePolicy(sizePolicy4)
        self.pushButton_color_green.setFont(font)
        self.pushButton_color_green.setStyleSheet(u"background-color: rgb(0, 255, 0);\n"
"                                                            ")

        self.horizontalLayout.addWidget(self.pushButton_color_green)

        self.pushButton_color_blue = QPushButton(self.widget)
        self.pushButton_color_blue.setObjectName(u"pushButton_color_blue")
        sizePolicy4.setHeightForWidth(self.pushButton_color_blue.sizePolicy().hasHeightForWidth())
        self.pushButton_color_blue.setSizePolicy(sizePolicy4)
        self.pushButton_color_blue.setFont(font)
        self.pushButton_color_blue.setStyleSheet(u"background-color: rgb(0, 0, 255);\n"
"                                                            ")

        self.horizontalLayout.addWidget(self.pushButton_color_blue)

        self.pushButton_color_yellow = QPushButton(self.widget)
        self.pushButton_color_yellow.setObjectName(u"pushButton_color_yellow")
        sizePolicy4.setHeightForWidth(self.pushButton_color_yellow.sizePolicy().hasHeightForWidth())
        self.pushButton_color_yellow.setSizePolicy(sizePolicy4)
        self.pushButton_color_yellow.setFont(font)
        self.pushButton_color_yellow.setStyleSheet(u"background-color: rgb(255, 255, 0);\n"
"                                                            ")

        self.horizontalLayout.addWidget(self.pushButton_color_yellow)

        self.pushButton_color_cyan = QPushButton(self.widget)
        self.pushButton_color_cyan.setObjectName(u"pushButton_color_cyan")
        sizePolicy4.setHeightForWidth(self.pushButton_color_cyan.sizePolicy().hasHeightForWidth())
        self.pushButton_color_cyan.setSizePolicy(sizePolicy4)
        self.pushButton_color_cyan.setFont(font)
        self.pushButton_color_cyan.setStyleSheet(u"background-color: rgb(0, 255, 255);\n"
"                                                            ")

        self.horizontalLayout.addWidget(self.pushButton_color_cyan)

        self.pushButton_color_purple = QPushButton(self.widget)
        self.pushButton_color_purple.setObjectName(u"pushButton_color_purple")
        sizePolicy4.setHeightForWidth(self.pushButton_color_purple.sizePolicy().hasHeightForWidth())
        self.pushButton_color_purple.setSizePolicy(sizePolicy4)
        self.pushButton_color_purple.setFont(font)
        self.pushButton_color_purple.setStyleSheet(u"background-color: rgb(255, 0, 255);\n"
"                                                            ")

        self.horizontalLayout.addWidget(self.pushButton_color_purple)

        self.pushButton_color_black = QPushButton(self.widget)
        self.pushButton_color_black.setObjectName(u"pushButton_color_black")
        sizePolicy4.setHeightForWidth(self.pushButton_color_black.sizePolicy().hasHeightForWidth())
        self.pushButton_color_black.setSizePolicy(sizePolicy4)
        self.pushButton_color_black.setFont(font)
        self.pushButton_color_black.setStyleSheet(u"background-color: rgb(0, 0, 0);")

        self.horizontalLayout.addWidget(self.pushButton_color_black)


        self.gridLayout_3.addWidget(self.widget, 0, 0, 1, 1)

        self.widget_2 = QWidget(self.groupBox_2)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setFont(font)
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_7 = QLabel(self.widget_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_7)

        self.spinBox_r = QSpinBox(self.widget_2)
        self.spinBox_r.setObjectName(u"spinBox_r")
        sizePolicy2.setHeightForWidth(self.spinBox_r.sizePolicy().hasHeightForWidth())
        self.spinBox_r.setSizePolicy(sizePolicy2)
        self.spinBox_r.setFont(font1)
        self.spinBox_r.setMaximum(255)

        self.horizontalLayout_2.addWidget(self.spinBox_r)

        self.label_8 = QLabel(self.widget_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_8)

        self.spinBox_g = QSpinBox(self.widget_2)
        self.spinBox_g.setObjectName(u"spinBox_g")
        sizePolicy2.setHeightForWidth(self.spinBox_g.sizePolicy().hasHeightForWidth())
        self.spinBox_g.setSizePolicy(sizePolicy2)
        self.spinBox_g.setFont(font1)
        self.spinBox_g.setMaximum(255)

        self.horizontalLayout_2.addWidget(self.spinBox_g)

        self.label_9 = QLabel(self.widget_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_9)

        self.spinBox_b = QSpinBox(self.widget_2)
        self.spinBox_b.setObjectName(u"spinBox_b")
        sizePolicy2.setHeightForWidth(self.spinBox_b.sizePolicy().hasHeightForWidth())
        self.spinBox_b.setSizePolicy(sizePolicy2)
        self.spinBox_b.setFont(font1)
        self.spinBox_b.setMaximum(255)

        self.horizontalLayout_2.addWidget(self.spinBox_b)


        self.gridLayout_3.addWidget(self.widget_2, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_2, 3, 0, 1, 2)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.lineEdit_Name.setText(QCoreApplication.translate("Dialog", u"New Point", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"**\u521b\u5efa\u65b0\u7684\u4f4d\u7f6e**", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u540d\u79f0\uff1a", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"\u4f4d\u7f6e\uff1a", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"X\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Y\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Z\uff1a", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"\u989c\u8272\uff1a", None))
        self.pushButton_color_red.setText("")
        self.pushButton_color_green.setText("")
        self.pushButton_color_blue.setText("")
        self.pushButton_color_yellow.setText("")
        self.pushButton_color_cyan.setText("")
        self.pushButton_color_purple.setText("")
        self.pushButton_color_black.setText("")
        self.label_7.setText(QCoreApplication.translate("Dialog", u"R", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"G", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"B", None))
    # retranslateUi

