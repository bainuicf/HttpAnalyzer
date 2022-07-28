# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QPushButton, QSizePolicy, QTextBrowser, QTextEdit,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setWindowModality(Qt.ApplicationModal)
        Form.resize(722, 530)
        icon = QIcon()
        icon.addFile(u"../../OneDrive/\u56fe\u7247/db7271a1bb4fb98f7303a5f6d1a7e2ee (2).png", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.horizontalLayout_5 = QHBoxLayout(Form)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.buttonAnylast = QPushButton(Form)
        self.buttonAnylast.setObjectName(u"buttonAnylast")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonAnylast.sizePolicy().hasHeightForWidth())
        self.buttonAnylast.setSizePolicy(sizePolicy)
        self.buttonAnylast.setSizeIncrement(QSize(0, 0))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.buttonAnylast.setFont(font)
        self.buttonAnylast.setAutoFillBackground(False)
        self.buttonAnylast.setAutoDefault(False)
        self.buttonAnylast.setFlat(False)

        self.gridLayout.addWidget(self.buttonAnylast, 0, 1, 3, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_1 = QLabel(Form)
        self.label_1.setObjectName(u"label_1")
        sizePolicy.setHeightForWidth(self.label_1.sizePolicy().hasHeightForWidth())
        self.label_1.setSizePolicy(sizePolicy)
        self.label_1.setFont(font)
        self.label_1.setFocusPolicy(Qt.NoFocus)
        self.label_1.setFrameShape(QFrame.Panel)
        self.label_1.setFrameShadow(QFrame.Sunken)
        self.label_1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_1)

        self.inputURL = QLineEdit(Form)
        self.inputURL.setObjectName(u"inputURL")
        sizePolicy.setHeightForWidth(self.inputURL.sizePolicy().hasHeightForWidth())
        self.inputURL.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(10)
        self.inputURL.setFont(font1)
        self.inputURL.setFrame(True)

        self.horizontalLayout.addWidget(self.inputURL)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 8)

        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setFont(font)
        self.label_4.setFocusPolicy(Qt.NoFocus)
        self.label_4.setFrameShape(QFrame.Panel)
        self.label_4.setFrameShadow(QFrame.Sunken)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_4)

        self.inputResult = QTextBrowser(Form)
        self.inputResult.setObjectName(u"inputResult")
        sizePolicy.setHeightForWidth(self.inputResult.sizePolicy().hasHeightForWidth())
        self.inputResult.setSizePolicy(sizePolicy)
        self.inputResult.setFont(font1)
        self.inputResult.setFrameShape(QFrame.Box)

        self.horizontalLayout_4.addWidget(self.inputResult)

        self.horizontalLayout_4.setStretch(0, 18)
        self.horizontalLayout_4.setStretch(1, 82)

        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 0, 1, 2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setFont(font)
        self.label_2.setFocusPolicy(Qt.NoFocus)
        self.label_2.setFrameShape(QFrame.Panel)
        self.label_2.setFrameShadow(QFrame.Sunken)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.inputMethod = QComboBox(Form)
        self.inputMethod.addItem("")
        self.inputMethod.addItem("")
        self.inputMethod.setObjectName(u"inputMethod")
        sizePolicy.setHeightForWidth(self.inputMethod.sizePolicy().hasHeightForWidth())
        self.inputMethod.setSizePolicy(sizePolicy)
        self.inputMethod.setFont(font)
        self.inputMethod.setLayoutDirection(Qt.LeftToRight)
        self.inputMethod.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)

        self.horizontalLayout_2.addWidget(self.inputMethod)

        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 8)

        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setFont(font)
        self.label_3.setFocusPolicy(Qt.NoFocus)
        self.label_3.setFrameShape(QFrame.Panel)
        self.label_3.setFrameShadow(QFrame.Sunken)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.inputOpt = QTextEdit(Form)
        self.inputOpt.setObjectName(u"inputOpt")
        sizePolicy.setHeightForWidth(self.inputOpt.sizePolicy().hasHeightForWidth())
        self.inputOpt.setSizePolicy(sizePolicy)
        self.inputOpt.setFont(font1)
        self.inputOpt.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.inputOpt.setFrameShape(QFrame.Box)
        self.inputOpt.setAcceptRichText(False)

        self.horizontalLayout_3.addWidget(self.inputOpt)

        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(1, 8)

        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)

        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setRowStretch(2, 2)
        self.gridLayout.setRowStretch(3, 9)
        self.gridLayout.setColumnStretch(0, 9)
        self.gridLayout.setColumnStretch(1, 1)

        self.horizontalLayout_5.addLayout(self.gridLayout)


        self.retranslateUi(Form)

        self.buttonAnylast.setDefault(True)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"HTTP\u5206\u6790\u5668  by ShellC", None))
        self.buttonAnylast.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb\u5206\u6790", None))
        self.label_1.setText(QCoreApplication.translate("Form", u"URL\u5730\u5740", None))
        self.inputURL.setPlaceholderText(QCoreApplication.translate("Form", u"\uff08\u8bf7\u8f93\u5165URL\u5730\u5740\uff0c\u683c\u5f0f\u4e3a\u201chttp(s)://www.baidu.com\u201d\uff09", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u8fd4\u56de\u7ed3\u679c", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u8bf7\u6c42\u65b9\u6cd5", None))
        self.inputMethod.setItemText(0, QCoreApplication.translate("Form", u"GET", None))
        self.inputMethod.setItemText(1, QCoreApplication.translate("Form", u"POST", None))

        self.label_3.setText(QCoreApplication.translate("Form", u"\u8bf7\u6c42\u53c2\u6570", None))
        self.inputOpt.setMarkdown("")
        self.inputOpt.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p></body></html>", None))
        self.inputOpt.setPlaceholderText(QCoreApplication.translate("Form", u"\uff08\u975e\u5fc5\u586b\u9879\uff0c\u683c\u5f0f\u4e3a\u201c\u53c2\u6570:(\u7a7a\u683c)\u5c5e\u6027\u201d\uff0c\u5efa\u8bae\u76f4\u63a5\u4ece\u6d4f\u89c8\u5668\u5f00\u53d1\u8005\u5de5\u5177\u590d\u5236\uff09", None))
    # retranslateUi

