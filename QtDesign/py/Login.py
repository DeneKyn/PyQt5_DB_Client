# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginForm.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


#from PyQt5 import QtCore, QtGui, QtWidgets
import PyQt5

class Ui_LoginWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(273, 172)
        MainWindow.setMinimumSize(PyQt5.QtCore.QSize(273, 0))
        MainWindow.setMouseTracking(False)
        MainWindow.setAnimated(True)
        self.centralwidget = PyQt5.QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_login = PyQt5.QtWidgets.QLabel(self.centralwidget)
        self.label_login.setGeometry(PyQt5.QtCore.QRect(20, 30, 45, 23))
        font = PyQt5.QtGui.QFont()
        font.setPointSize(14)
        self.label_login.setFont(font)
        self.label_login.setObjectName("label_login")
        self.btn_register = PyQt5.QtWidgets.QPushButton(self.centralwidget)
        self.btn_register.setGeometry(PyQt5.QtCore.QRect(160, 110, 101, 31))
        self.btn_register.setObjectName("btn_register")
        self.label_password = PyQt5.QtWidgets.QLabel(self.centralwidget)
        self.label_password.setGeometry(PyQt5.QtCore.QRect(10, 70, 78, 23))
        font = PyQt5.QtGui.QFont()
        font.setPointSize(14)
        self.label_password.setFont(font)
        self.label_password.setObjectName("label_password")
        self.edit_password = PyQt5.QtWidgets.QLineEdit(self.centralwidget)
        self.edit_password.setGeometry(PyQt5.QtCore.QRect(100, 70, 161, 21))
        self.edit_password.setEchoMode(PyQt5.QtWidgets.QLineEdit.Password)
        self.edit_password.setObjectName("edit_password")
        self.btn_login = PyQt5.QtWidgets.QPushButton(self.centralwidget)
        self.btn_login.setGeometry(PyQt5.QtCore.QRect(20, 110, 101, 31))
        self.btn_login.setObjectName("btn_login")
        self.edit_login = PyQt5.QtWidgets.QLineEdit(self.centralwidget)
        self.edit_login.setGeometry(PyQt5.QtCore.QRect(99, 27, 161, 21))
        self.edit_login.setObjectName("edit_login")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = PyQt5.QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        PyQt5.QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.edit_login, self.edit_password)
        MainWindow.setTabOrder(self.edit_password, self.btn_login)
        MainWindow.setTabOrder(self.btn_login, self.btn_register)

    def retranslateUi(self, MainWindow):
        _translate = PyQt5.QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.label_login.setText(_translate("MainWindow", "Login"))
        self.btn_register.setText(_translate("MainWindow", "Register"))
        self.label_password.setText(_translate("MainWindow", "Password"))
        self.btn_login.setText(_translate("MainWindow", "Login"))
