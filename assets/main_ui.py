# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSpinBox, QVBoxLayout,
    QWidget)
from  . import rc_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(263, 220)
        MainWindow.setMinimumSize(QSize(260, 220))
        icon = QIcon()
        icon.addFile(u":/img/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.paras = QWidget(self.centralwidget)
        self.paras.setObjectName(u"paras")
        self.paras.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.paras)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.paras)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(40, 0))

        self.horizontalLayout_2.addWidget(self.label)

        self.vA = QSpinBox(self.widget_3)
        self.vA.setObjectName(u"vA")
        self.vA.setMaximum(1000)

        self.horizontalLayout_2.addWidget(self.vA)


        self.verticalLayout_2.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.paras)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget_4)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QSize(40, 0))

        self.horizontalLayout_3.addWidget(self.label_2)

        self.vE1 = QSpinBox(self.widget_4)
        self.vE1.setObjectName(u"vE1")
        self.vE1.setMaximum(1000)

        self.horizontalLayout_3.addWidget(self.vE1)


        self.verticalLayout_2.addWidget(self.widget_4)

        self.widget_7 = QWidget(self.paras)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.widget_7)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QSize(40, 0))

        self.horizontalLayout_6.addWidget(self.label_5)

        self.vE2 = QSpinBox(self.widget_7)
        self.vE2.setObjectName(u"vE2")
        self.vE2.setMaximum(1000)

        self.horizontalLayout_6.addWidget(self.vE2)


        self.verticalLayout_2.addWidget(self.widget_7)

        self.widget_8 = QWidget(self.paras)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.widget_8)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QSize(40, 0))

        self.horizontalLayout_7.addWidget(self.label_6)

        self.vE3 = QSpinBox(self.widget_8)
        self.vE3.setObjectName(u"vE3")
        self.vE3.setMaximum(1000)

        self.horizontalLayout_7.addWidget(self.vE3)


        self.verticalLayout_2.addWidget(self.widget_8)

        self.widget_5 = QWidget(self.paras)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.widget_5)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QSize(40, 0))

        self.horizontalLayout_4.addWidget(self.label_3)

        self.vSH = QSpinBox(self.widget_5)
        self.vSH.setObjectName(u"vSH")
        self.vSH.setMaximum(1000)

        self.horizontalLayout_4.addWidget(self.vSH)


        self.verticalLayout_2.addWidget(self.widget_5)


        self.verticalLayout.addWidget(self.paras)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.Block = QPushButton(self.widget)
        self.Block.setObjectName(u"Block")

        self.verticalLayout_3.addWidget(self.Block)

        self.Bstart = QPushButton(self.widget)
        self.Bstart.setObjectName(u"Bstart")

        self.verticalLayout_3.addWidget(self.Bstart)

        self.Bstop = QPushButton(self.widget)
        self.Bstop.setObjectName(u"Bstop")

        self.verticalLayout_3.addWidget(self.Bstop)


        self.verticalLayout.addWidget(self.widget)

        self.info = QLabel(self.centralwidget)
        self.info.setObjectName(u"info")

        self.verticalLayout.addWidget(self.info)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.Bstart, self.Bstop)
        QWidget.setTabOrder(self.Bstop, self.vE1)
        QWidget.setTabOrder(self.vE1, self.vA)
        QWidget.setTabOrder(self.vA, self.vE2)
        QWidget.setTabOrder(self.vE2, self.vE3)
        QWidget.setTabOrder(self.vE3, self.vSH)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u767b\u9f99\u65a9\u5c0f\u52a9\u624b", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"E1", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"E2", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"E3", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Shift", None))
        self.Block.setText(QCoreApplication.translate("MainWindow", u"\u53c2\u6570", None))
        self.Bstart.setText(QCoreApplication.translate("MainWindow", u"\u542f\u52a8", None))
        self.Bstop.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed", None))
        self.info.setText(QCoreApplication.translate("MainWindow", u"info", None))
    # retranslateUi

