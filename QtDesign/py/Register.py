# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RegisterForm.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(313, 459)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.LoginAndPass = QtWidgets.QFrame(self.centralwidget)
        self.LoginAndPass.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LoginAndPass.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LoginAndPass.setObjectName("LoginAndPass")
        self.gridLayout = QtWidgets.QGridLayout(self.LoginAndPass)
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_login = QtWidgets.QLabel(self.LoginAndPass)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_login.setFont(font)
        self.lbl_login.setObjectName("lbl_login")
        self.gridLayout.addWidget(self.lbl_login, 0, 0, 1, 1)
        self.edit_login = QtWidgets.QLineEdit(self.LoginAndPass)
        self.edit_login.setObjectName("edit_login")
        self.gridLayout.addWidget(self.edit_login, 0, 1, 1, 1)
        self.lbl_password = QtWidgets.QLabel(self.LoginAndPass)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_password.setFont(font)
        self.lbl_password.setObjectName("lbl_password")
        self.gridLayout.addWidget(self.lbl_password, 1, 0, 1, 1)
        self.edit_password = QtWidgets.QLineEdit(self.LoginAndPass)
        self.edit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.edit_password.setObjectName("edit_password")
        self.gridLayout.addWidget(self.edit_password, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.LoginAndPass)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lbl_name2 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_name2.setFont(font)
        self.lbl_name2.setObjectName("lbl_name2")
        self.gridLayout_2.addWidget(self.lbl_name2, 0, 0, 1, 1)
        self.edit_name2 = QtWidgets.QLineEdit(self.frame_2)
        self.edit_name2.setObjectName("edit_name2")
        self.gridLayout_2.addWidget(self.edit_name2, 0, 1, 1, 1)
        self.lbl_name1 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_name1.setFont(font)
        self.lbl_name1.setObjectName("lbl_name1")
        self.gridLayout_2.addWidget(self.lbl_name1, 1, 0, 1, 1)
        self.edit_name1 = QtWidgets.QLineEdit(self.frame_2)
        self.edit_name1.setObjectName("edit_name1")
        self.gridLayout_2.addWidget(self.edit_name1, 1, 1, 1, 1)
        self.lbl_name3 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_name3.setFont(font)
        self.lbl_name3.setObjectName("lbl_name3")
        self.gridLayout_2.addWidget(self.lbl_name3, 2, 0, 1, 1)
        self.edit_name3 = QtWidgets.QLineEdit(self.frame_2)
        self.edit_name3.setObjectName("edit_name3")
        self.gridLayout_2.addWidget(self.edit_name3, 2, 1, 1, 1)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lbl_select = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_select.setFont(font)
        self.lbl_select.setObjectName("lbl_select")
        self.gridLayout_3.addWidget(self.lbl_select, 0, 0, 1, 1)
        self.rBtn_client = QtWidgets.QRadioButton(self.frame)
        self.rBtn_client.setObjectName("rBtn_client")
        self.gridLayout_3.addWidget(self.rBtn_client, 1, 0, 1, 1)
        self.rBtn_provider = QtWidgets.QRadioButton(self.frame)
        self.rBtn_provider.setObjectName("rBtn_provider")
        self.gridLayout_3.addWidget(self.rBtn_provider, 2, 0, 1, 1)
        self.rBtn_admin = QtWidgets.QRadioButton(self.frame)
        self.rBtn_admin.setObjectName("rBtn_admin")
        self.gridLayout_3.addWidget(self.rBtn_admin, 3, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        self.btn_register = QtWidgets.QPushButton(self.centralwidget)
        self.btn_register.setObjectName("btn_register")
        self.verticalLayout.addWidget(self.btn_register)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbl_login.setText(_translate("MainWindow", "Login"))
        self.lbl_password.setText(_translate("MainWindow", "Password"))
        self.lbl_name2.setText(_translate("MainWindow", "First name"))
        self.lbl_name1.setText(_translate("MainWindow", "Last name"))
        self.lbl_name3.setText(_translate("MainWindow", "Patronymic"))
        self.lbl_select.setText(_translate("MainWindow", "Select a user type"))
        self.rBtn_client.setText(_translate("MainWindow", "Client"))
        self.rBtn_provider.setText(_translate("MainWindow", "Provider"))
        self.rBtn_admin.setText(_translate("MainWindow", "Admin"))
        self.btn_register.setText(_translate("MainWindow", "Register"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
