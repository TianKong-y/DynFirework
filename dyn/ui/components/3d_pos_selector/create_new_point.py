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
    QDoubleSpinBox, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpinBox, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(577, 393)
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
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_2, 3, 0, 1, 1)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 1)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamilies([u"Ark Pixel 12px P zh_cn"])
        font1.setPointSize(24)
        self.label_4.setFont(font1)
        self.label_4.setTextFormat(Qt.TextFormat.MarkdownText)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 2)

        self.doubleSpinBox_Z = QDoubleSpinBox(self.frame)
        self.doubleSpinBox_Z.setObjectName(u"doubleSpinBox_Z")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.doubleSpinBox_Z.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_Z.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setFamilies([u"Ubuntu"])
        self.doubleSpinBox_Z.setFont(font2)
        self.doubleSpinBox_Z.setMinimum(-200.000000000000000)
        self.doubleSpinBox_Z.setMaximum(200.000000000000000)

        self.gridLayout_2.addWidget(self.doubleSpinBox_Z, 4, 1, 1, 1)

        self.lineEdit_Name = QLineEdit(self.frame)
        self.lineEdit_Name.setObjectName(u"lineEdit_Name")
        self.lineEdit_Name.setFont(font2)

        self.gridLayout_2.addWidget(self.lineEdit_Name, 1, 1, 1, 1)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_3, 4, 0, 1, 1)

        self.doubleSpinBox_X = QDoubleSpinBox(self.frame)
        self.doubleSpinBox_X.setObjectName(u"doubleSpinBox_X")
        sizePolicy2.setHeightForWidth(self.doubleSpinBox_X.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_X.setSizePolicy(sizePolicy2)
        self.doubleSpinBox_X.setFont(font2)
        self.doubleSpinBox_X.setMinimum(-200.000000000000000)
        self.doubleSpinBox_X.setMaximum(200.000000000000000)

        self.gridLayout_2.addWidget(self.doubleSpinBox_X, 2, 1, 1, 1)

        self.doubleSpinBox_Y = QDoubleSpinBox(self.frame)
        self.doubleSpinBox_Y.setObjectName(u"doubleSpinBox_Y")
        sizePolicy2.setHeightForWidth(self.doubleSpinBox_Y.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_Y.setSizePolicy(sizePolicy2)
        self.doubleSpinBox_Y.setFont(font2)
        self.doubleSpinBox_Y.setMaximum(320.000000000000000)
        self.doubleSpinBox_Y.setValue(80.000000000000000)

        self.gridLayout_2.addWidget(self.doubleSpinBox_Y, 3, 1, 1, 1)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setFont(font)
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_6, 5, 0, 1, 1)

        self.widget_2 = QWidget(self.frame)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy3)
        self.widget_2.setFont(font)
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(self.widget_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"background-color: rgb(255, 0, 0);")

        self.horizontalLayout.addWidget(self.pushButton)

        self.label_7 = QLabel(self.widget_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_7)

        self.spinBox_r = QSpinBox(self.widget_2)
        self.spinBox_r.setObjectName(u"spinBox_r")
        sizePolicy2.setHeightForWidth(self.spinBox_r.sizePolicy().hasHeightForWidth())
        self.spinBox_r.setSizePolicy(sizePolicy2)
        self.spinBox_r.setFont(font2)
        self.spinBox_r.setMaximum(255)
        self.spinBox_r.setValue(255)

        self.horizontalLayout.addWidget(self.spinBox_r)

        self.label_8 = QLabel(self.widget_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_8)

        self.spinBox_g = QSpinBox(self.widget_2)
        self.spinBox_g.setObjectName(u"spinBox_g")
        sizePolicy2.setHeightForWidth(self.spinBox_g.sizePolicy().hasHeightForWidth())
        self.spinBox_g.setSizePolicy(sizePolicy2)
        self.spinBox_g.setFont(font2)
        self.spinBox_g.setMaximum(255)

        self.horizontalLayout.addWidget(self.spinBox_g)

        self.label_9 = QLabel(self.widget_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_9)

        self.spinBox_b = QSpinBox(self.widget_2)
        self.spinBox_b.setObjectName(u"spinBox_b")
        sizePolicy2.setHeightForWidth(self.spinBox_b.sizePolicy().hasHeightForWidth())
        self.spinBox_b.setSizePolicy(sizePolicy2)
        self.spinBox_b.setFont(font2)
        self.spinBox_b.setMaximum(255)

        self.horizontalLayout.addWidget(self.spinBox_b)


        self.gridLayout_2.addWidget(self.widget_2, 5, 1, 1, 1)


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
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Y\uff1a", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"X\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"**\u521b\u5efa\u65b0\u7684\u4f4d\u7f6e\u70b9**", None))
        self.lineEdit_Name.setText(QCoreApplication.translate("Dialog", u"New Point", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u540d\u79f0\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Z\uff1a", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"\u989c\u8272\uff1a", None))
        self.pushButton.setText("")
        self.label_7.setText(QCoreApplication.translate("Dialog", u"R", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"G", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"B", None))
    # retranslateUi

