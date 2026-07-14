# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_new_line.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QDoubleSpinBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(686, 691)
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
        self.label_name = QLabel(self.frame)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_name.sizePolicy().hasHeightForWidth())
        self.label_name.setSizePolicy(sizePolicy)
        self.label_name.setFont(font)
        self.label_name.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_name, 1, 0, 1, 1)

        self.groupBox_start = QGroupBox(self.frame)
        self.groupBox_start.setObjectName(u"groupBox_start")
        self.groupBox_start.setEnabled(False)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_start.sizePolicy().hasHeightForWidth())
        self.groupBox_start.setSizePolicy(sizePolicy1)
        self.gridLayout_4 = QGridLayout(self.groupBox_start)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_X_start = QLabel(self.groupBox_start)
        self.label_X_start.setObjectName(u"label_X_start")
        sizePolicy1.setHeightForWidth(self.label_X_start.sizePolicy().hasHeightForWidth())
        self.label_X_start.setSizePolicy(sizePolicy1)
        self.label_X_start.setFont(font)
        self.label_X_start.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_X_start, 0, 0, 1, 1)

        self.doubleSpinBox_X_start = QDoubleSpinBox(self.groupBox_start)
        self.doubleSpinBox_X_start.setObjectName(u"doubleSpinBox_X_start")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.doubleSpinBox_X_start.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_X_start.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setFamilies([u"Ubuntu"])
        self.doubleSpinBox_X_start.setFont(font1)
        self.doubleSpinBox_X_start.setMinimum(-200.000000000000000)
        self.doubleSpinBox_X_start.setMaximum(200.000000000000000)

        self.gridLayout_4.addWidget(self.doubleSpinBox_X_start, 0, 1, 1, 1)

        self.label_Y_start = QLabel(self.groupBox_start)
        self.label_Y_start.setObjectName(u"label_Y_start")
        sizePolicy1.setHeightForWidth(self.label_Y_start.sizePolicy().hasHeightForWidth())
        self.label_Y_start.setSizePolicy(sizePolicy1)
        self.label_Y_start.setFont(font)
        self.label_Y_start.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_Y_start, 1, 0, 1, 1)

        self.doubleSpinBox_Y_start = QDoubleSpinBox(self.groupBox_start)
        self.doubleSpinBox_Y_start.setObjectName(u"doubleSpinBox_Y_start")
        sizePolicy2.setHeightForWidth(self.doubleSpinBox_Y_start.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_Y_start.setSizePolicy(sizePolicy2)
        self.doubleSpinBox_Y_start.setFont(font1)
        self.doubleSpinBox_Y_start.setMaximum(320.000000000000000)
        self.doubleSpinBox_Y_start.setValue(80.000000000000000)

        self.gridLayout_4.addWidget(self.doubleSpinBox_Y_start, 1, 1, 1, 1)

        self.label_Z_start = QLabel(self.groupBox_start)
        self.label_Z_start.setObjectName(u"label_Z_start")
        sizePolicy1.setHeightForWidth(self.label_Z_start.sizePolicy().hasHeightForWidth())
        self.label_Z_start.setSizePolicy(sizePolicy1)
        self.label_Z_start.setFont(font)
        self.label_Z_start.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_Z_start, 2, 0, 1, 1)

        self.doubleSpinBox_Z_start = QDoubleSpinBox(self.groupBox_start)
        self.doubleSpinBox_Z_start.setObjectName(u"doubleSpinBox_Z_start")
        sizePolicy2.setHeightForWidth(self.doubleSpinBox_Z_start.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_Z_start.setSizePolicy(sizePolicy2)
        self.doubleSpinBox_Z_start.setFont(font1)
        self.doubleSpinBox_Z_start.setMinimum(-200.000000000000000)
        self.doubleSpinBox_Z_start.setMaximum(200.000000000000000)

        self.gridLayout_4.addWidget(self.doubleSpinBox_Z_start, 2, 1, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_start, 2, 0, 1, 2)

        self.groupBox_end = QGroupBox(self.frame)
        self.groupBox_end.setObjectName(u"groupBox_end")
        sizePolicy1.setHeightForWidth(self.groupBox_end.sizePolicy().hasHeightForWidth())
        self.groupBox_end.setSizePolicy(sizePolicy1)
        self.gridLayout_3 = QGridLayout(self.groupBox_end)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.doubleSpinBox_Z_end = QDoubleSpinBox(self.groupBox_end)
        self.doubleSpinBox_Z_end.setObjectName(u"doubleSpinBox_Z_end")
        sizePolicy2.setHeightForWidth(self.doubleSpinBox_Z_end.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_Z_end.setSizePolicy(sizePolicy2)
        self.doubleSpinBox_Z_end.setFont(font1)
        self.doubleSpinBox_Z_end.setMinimum(-200.000000000000000)
        self.doubleSpinBox_Z_end.setMaximum(200.000000000000000)

        self.gridLayout_3.addWidget(self.doubleSpinBox_Z_end, 2, 1, 1, 1)

        self.label_Z_end = QLabel(self.groupBox_end)
        self.label_Z_end.setObjectName(u"label_Z_end")
        sizePolicy1.setHeightForWidth(self.label_Z_end.sizePolicy().hasHeightForWidth())
        self.label_Z_end.setSizePolicy(sizePolicy1)
        self.label_Z_end.setFont(font)
        self.label_Z_end.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_Z_end, 2, 0, 1, 1)

        self.label_X_end = QLabel(self.groupBox_end)
        self.label_X_end.setObjectName(u"label_X_end")
        sizePolicy1.setHeightForWidth(self.label_X_end.sizePolicy().hasHeightForWidth())
        self.label_X_end.setSizePolicy(sizePolicy1)
        self.label_X_end.setFont(font)
        self.label_X_end.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_X_end, 0, 0, 1, 1)

        self.doubleSpinBox_Y_end = QDoubleSpinBox(self.groupBox_end)
        self.doubleSpinBox_Y_end.setObjectName(u"doubleSpinBox_Y_end")
        sizePolicy2.setHeightForWidth(self.doubleSpinBox_Y_end.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_Y_end.setSizePolicy(sizePolicy2)
        self.doubleSpinBox_Y_end.setFont(font1)
        self.doubleSpinBox_Y_end.setMaximum(320.000000000000000)
        self.doubleSpinBox_Y_end.setValue(80.000000000000000)

        self.gridLayout_3.addWidget(self.doubleSpinBox_Y_end, 1, 1, 1, 1)

        self.doubleSpinBox_X_end = QDoubleSpinBox(self.groupBox_end)
        self.doubleSpinBox_X_end.setObjectName(u"doubleSpinBox_X_end")
        sizePolicy2.setHeightForWidth(self.doubleSpinBox_X_end.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_X_end.setSizePolicy(sizePolicy2)
        self.doubleSpinBox_X_end.setFont(font1)
        self.doubleSpinBox_X_end.setMinimum(-200.000000000000000)
        self.doubleSpinBox_X_end.setMaximum(200.000000000000000)

        self.gridLayout_3.addWidget(self.doubleSpinBox_X_end, 0, 1, 1, 1)

        self.label_Y_end = QLabel(self.groupBox_end)
        self.label_Y_end.setObjectName(u"label_Y_end")
        sizePolicy1.setHeightForWidth(self.label_Y_end.sizePolicy().hasHeightForWidth())
        self.label_Y_end.setSizePolicy(sizePolicy1)
        self.label_Y_end.setFont(font)
        self.label_Y_end.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_Y_end, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_end, 3, 0, 1, 2)

        self.groupBox_color = QGroupBox(self.frame)
        self.groupBox_color.setObjectName(u"groupBox_color")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.groupBox_color.sizePolicy().hasHeightForWidth())
        self.groupBox_color.setSizePolicy(sizePolicy3)
        self.groupBox_color.setFont(font)
        self.verticalLayout = QVBoxLayout(self.groupBox_color)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.checkBox_enable_gradient = QCheckBox(self.groupBox_color)
        self.checkBox_enable_gradient.setObjectName(u"checkBox_enable_gradient")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.checkBox_enable_gradient.sizePolicy().hasHeightForWidth())
        self.checkBox_enable_gradient.setSizePolicy(sizePolicy4)

        self.verticalLayout.addWidget(self.checkBox_enable_gradient)

        self.widget_start = QWidget(self.groupBox_color)
        self.widget_start.setObjectName(u"widget_start")
        self.horizontalLayout = QHBoxLayout(self.widget_start)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_start = QLabel(self.widget_start)
        self.label_start.setObjectName(u"label_start")
        self.label_start.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_start)

        self.color_selector_start = QPushButton(self.widget_start)
        self.color_selector_start.setObjectName(u"color_selector_start")
        self.color_selector_start.setStyleSheet(u"background-color: rgb(255, 0, 0);")

        self.horizontalLayout.addWidget(self.color_selector_start)

        self.label_r_start = QLabel(self.widget_start)
        self.label_r_start.setObjectName(u"label_r_start")
        self.label_r_start.setFont(font)
        self.label_r_start.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_r_start)

        self.spinBox_r_start = QSpinBox(self.widget_start)
        self.spinBox_r_start.setObjectName(u"spinBox_r_start")
        sizePolicy.setHeightForWidth(self.spinBox_r_start.sizePolicy().hasHeightForWidth())
        self.spinBox_r_start.setSizePolicy(sizePolicy)
        self.spinBox_r_start.setFont(font1)
        self.spinBox_r_start.setMaximum(255)
        self.spinBox_r_start.setValue(255)

        self.horizontalLayout.addWidget(self.spinBox_r_start)

        self.label_g_start = QLabel(self.widget_start)
        self.label_g_start.setObjectName(u"label_g_start")
        self.label_g_start.setFont(font)
        self.label_g_start.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_g_start)

        self.spinBox_g_start = QSpinBox(self.widget_start)
        self.spinBox_g_start.setObjectName(u"spinBox_g_start")
        sizePolicy.setHeightForWidth(self.spinBox_g_start.sizePolicy().hasHeightForWidth())
        self.spinBox_g_start.setSizePolicy(sizePolicy)
        self.spinBox_g_start.setFont(font1)
        self.spinBox_g_start.setMaximum(255)

        self.horizontalLayout.addWidget(self.spinBox_g_start)

        self.label_b_sart = QLabel(self.widget_start)
        self.label_b_sart.setObjectName(u"label_b_sart")
        self.label_b_sart.setFont(font)
        self.label_b_sart.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_b_sart)

        self.spinBox_b_start = QSpinBox(self.widget_start)
        self.spinBox_b_start.setObjectName(u"spinBox_b_start")
        sizePolicy.setHeightForWidth(self.spinBox_b_start.sizePolicy().hasHeightForWidth())
        self.spinBox_b_start.setSizePolicy(sizePolicy)
        self.spinBox_b_start.setFont(font1)
        self.spinBox_b_start.setMaximum(255)

        self.horizontalLayout.addWidget(self.spinBox_b_start)


        self.verticalLayout.addWidget(self.widget_start)

        self.widget_end = QWidget(self.groupBox_color)
        self.widget_end.setObjectName(u"widget_end")
        self.widget_end.setEnabled(False)
        self.horizontalLayout_2 = QHBoxLayout(self.widget_end)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_end = QLabel(self.widget_end)
        self.label_end.setObjectName(u"label_end")
        self.label_end.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_end)

        self.color_selector_end = QPushButton(self.widget_end)
        self.color_selector_end.setObjectName(u"color_selector_end")
        self.color_selector_end.setStyleSheet(u"background-color: rgb(0, 255, 0);")

        self.horizontalLayout_2.addWidget(self.color_selector_end)

        self.label_r_end = QLabel(self.widget_end)
        self.label_r_end.setObjectName(u"label_r_end")
        self.label_r_end.setFont(font)
        self.label_r_end.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_r_end)

        self.spinBox_r_3 = QSpinBox(self.widget_end)
        self.spinBox_r_3.setObjectName(u"spinBox_r_3")
        sizePolicy.setHeightForWidth(self.spinBox_r_3.sizePolicy().hasHeightForWidth())
        self.spinBox_r_3.setSizePolicy(sizePolicy)
        self.spinBox_r_3.setFont(font1)
        self.spinBox_r_3.setMaximum(255)
        self.spinBox_r_3.setValue(0)

        self.horizontalLayout_2.addWidget(self.spinBox_r_3)

        self.label_g_end = QLabel(self.widget_end)
        self.label_g_end.setObjectName(u"label_g_end")
        self.label_g_end.setFont(font)
        self.label_g_end.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_g_end)

        self.spinBox_g_3 = QSpinBox(self.widget_end)
        self.spinBox_g_3.setObjectName(u"spinBox_g_3")
        sizePolicy.setHeightForWidth(self.spinBox_g_3.sizePolicy().hasHeightForWidth())
        self.spinBox_g_3.setSizePolicy(sizePolicy)
        self.spinBox_g_3.setFont(font1)
        self.spinBox_g_3.setMaximum(255)
        self.spinBox_g_3.setValue(255)

        self.horizontalLayout_2.addWidget(self.spinBox_g_3)

        self.label_b_end = QLabel(self.widget_end)
        self.label_b_end.setObjectName(u"label_b_end")
        self.label_b_end.setFont(font)
        self.label_b_end.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_b_end)

        self.spinBox_b_3 = QSpinBox(self.widget_end)
        self.spinBox_b_3.setObjectName(u"spinBox_b_3")
        sizePolicy.setHeightForWidth(self.spinBox_b_3.sizePolicy().hasHeightForWidth())
        self.spinBox_b_3.setSizePolicy(sizePolicy)
        self.spinBox_b_3.setFont(font1)
        self.spinBox_b_3.setMaximum(255)

        self.horizontalLayout_2.addWidget(self.spinBox_b_3)


        self.verticalLayout.addWidget(self.widget_end)


        self.gridLayout_2.addWidget(self.groupBox_color, 4, 0, 1, 2)

        self.label_new_line = QLabel(self.frame)
        self.label_new_line.setObjectName(u"label_new_line")
        sizePolicy4.setHeightForWidth(self.label_new_line.sizePolicy().hasHeightForWidth())
        self.label_new_line.setSizePolicy(sizePolicy4)
        font2 = QFont()
        font2.setFamilies([u"Ark Pixel 12px P zh_cn"])
        font2.setPointSize(24)
        self.label_new_line.setFont(font2)
        self.label_new_line.setTextFormat(Qt.TextFormat.MarkdownText)
        self.label_new_line.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_new_line, 0, 0, 1, 3)

        self.groupBox_preview = QGroupBox(self.frame)
        self.groupBox_preview.setObjectName(u"groupBox_preview")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.groupBox_preview.sizePolicy().hasHeightForWidth())
        self.groupBox_preview.setSizePolicy(sizePolicy5)
        self.groupBox_preview.setMinimumSize(QSize(200, 0))

        self.gridLayout_2.addWidget(self.groupBox_preview, 2, 2, 3, 1)

        self.lineEdit_Name = QLineEdit(self.frame)
        self.lineEdit_Name.setObjectName(u"lineEdit_Name")
        self.lineEdit_Name.setFont(font1)

        self.gridLayout_2.addWidget(self.lineEdit_Name, 1, 1, 1, 2)


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
        self.checkBox_enable_gradient.toggled.connect(self.widget_end.setVisible)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_name.setText(QCoreApplication.translate("Dialog", u"\u540d\u79f0\uff1a", None))
        self.groupBox_start.setTitle(QCoreApplication.translate("Dialog", u"\u9009\u4e2d\u4f4d\u7f6e", None))
        self.label_X_start.setText(QCoreApplication.translate("Dialog", u"X\uff1a", None))
        self.label_Y_start.setText(QCoreApplication.translate("Dialog", u"Y\uff1a", None))
        self.label_Z_start.setText(QCoreApplication.translate("Dialog", u"Z\uff1a", None))
        self.groupBox_end.setTitle(QCoreApplication.translate("Dialog", u"\u76ee\u6807\u70b9", None))
        self.label_Z_end.setText(QCoreApplication.translate("Dialog", u"Z\uff1a", None))
        self.label_X_end.setText(QCoreApplication.translate("Dialog", u"X\uff1a", None))
        self.label_Y_end.setText(QCoreApplication.translate("Dialog", u"Y\uff1a", None))
        self.groupBox_color.setTitle(QCoreApplication.translate("Dialog", u"\u989c\u8272", None))
        self.checkBox_enable_gradient.setText(QCoreApplication.translate("Dialog", u"\u542f\u7528\u6e10\u53d8", None))
        self.label_start.setText(QCoreApplication.translate("Dialog", u"\u8d77\u59cb\u989c\u8272", None))
        self.color_selector_start.setText("")
        self.label_r_start.setText(QCoreApplication.translate("Dialog", u"R", None))
        self.label_g_start.setText(QCoreApplication.translate("Dialog", u"G", None))
        self.label_b_sart.setText(QCoreApplication.translate("Dialog", u"B", None))
        self.label_end.setText(QCoreApplication.translate("Dialog", u"\u76ee\u6807\u989c\u8272", None))
        self.color_selector_end.setText("")
        self.label_r_end.setText(QCoreApplication.translate("Dialog", u"R", None))
        self.label_g_end.setText(QCoreApplication.translate("Dialog", u"G", None))
        self.label_b_end.setText(QCoreApplication.translate("Dialog", u"B", None))
        self.label_new_line.setText(QCoreApplication.translate("Dialog", u"**\u521b\u5efa\u8f85\u52a9\u7ebf**", None))
        self.groupBox_preview.setTitle(QCoreApplication.translate("Dialog", u"\u9884\u89c8", None))
        self.lineEdit_Name.setText(QCoreApplication.translate("Dialog", u"New Line", None))
    # retranslateUi

