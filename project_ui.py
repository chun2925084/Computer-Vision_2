# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\hw1.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(682, 422)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(50, 50, 341, 181))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")

        #btn1_1
        self.btn1_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn1_1.setGeometry(QtCore.QRect(60, 50, 180, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.btn1_1.setFont(font)
        self.btn1_1.setObjectName("btn1_1")
        
        # #btn1_2
        self.btn1_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn1_2.setGeometry(QtCore.QRect(60, 115, 180, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.btn1_2.setFont(font)
        self.btn1_2.setObjectName("btn1_2")

        # #btn1_3
        self.btn1_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn1_3.setGeometry(QtCore.QRect(60, 180, 180, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.btn1_3.setFont(font)
        self.btn1_3.setObjectName("btn1_3")

        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(50, 270, 341, 100))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_2.setObjectName("frame_2")

        # #btn2_1
        self.btn2_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn2_1.setGeometry(QtCore.QRect(60, 280, 230, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.btn2_1.setFont(font)
        self.btn2_1.setObjectName("btn2_1")

        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(410, 50, 261, 321))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_3.setObjectName("frame_3")

        #btn3_1
        self.btn3_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn3_1.setGeometry(QtCore.QRect(430, 60, 180, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.btn3_1.setFont(font)
        self.btn3_1.setObjectName("btn3_1")

        # #btn3_2
        self.btn3_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn3_2.setGeometry(QtCore.QRect(430, 130, 200, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.btn3_2.setFont(font)
        self.btn3_2.setObjectName("btn3_2")

        # #label for Q1
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")

        # #labe for Q2
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 240, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        # #label for Q3
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(400, 20, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 682, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn1_1.setText(_translate("MainWindow", "1.1 Feature patch"))
        self.btn1_3.setText(_translate("MainWindow", "1.3 Find Corners"))
        self.btn2_1.setText(_translate(
            "MainWindow", "2.1 Bacjground substraction"))
        self.btn1_2.setText(_translate("MainWindow", "1.2 Feature points"))
        self.btn3_1.setText(_translate("MainWindow", "3.1 Preprocessing"))
        self.btn3_2.setText(_translate("MainWindow", "3.2 Perspective Transform"))
        self.label.setText(_translate("MainWindow", "1. SIFT"))
        self.label_2.setText(_translate("MainWindow", "2. Background subtraction"))
        self.label_3.setText(_translate(
            "MainWindow", "3. Feature tracking"))
     

