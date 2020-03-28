# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UserChange.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UserChange(object):
    def setupUi(self, UserChange):
        UserChange.setObjectName("UserChange")
        UserChange.resize(388, 183)
        self.centralwidget = QtWidgets.QWidget(UserChange)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lbl_login = QtWidgets.QLabel(self.centralwidget)
        self.lbl_login.setMinimumSize(QtCore.QSize(0, 23))
        self.lbl_login.setMaximumSize(QtCore.QSize(16777215, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_login.setFont(font)
        self.lbl_login.setObjectName("lbl_login")
        self.verticalLayout_2.addWidget(self.lbl_login)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_unlock = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_unlock.setObjectName("btn_unlock")
        self.gridLayout.addWidget(self.btn_unlock, 0, 0, 1, 2)
        self.btn_lock = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_lock.setObjectName("btn_lock")
        self.gridLayout.addWidget(self.btn_lock, 1, 0, 1, 2)
        self.btn_time_block = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_time_block.setObjectName("btn_time_block")
        self.gridLayout.addWidget(self.btn_time_block, 2, 0, 1, 1)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.groupBox_2)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.gridLayout.addWidget(self.dateTimeEdit, 2, 1, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_2, 0, 0, 2, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.comboBox_userType = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_userType.setObjectName("comboBox_userType")
        self.comboBox_userType.addItem("")
        self.comboBox_userType.addItem("")
        self.comboBox_userType.addItem("")
        self.verticalLayout.addWidget(self.comboBox_userType)
        self.btn_apply = QtWidgets.QPushButton(self.groupBox)
        self.btn_apply.setObjectName("btn_apply")
        self.verticalLayout.addWidget(self.btn_apply)
        self.gridLayout_2.addWidget(self.groupBox, 0, 1, 1, 1)
        self.btn_delete = QtWidgets.QPushButton(self.centralwidget)
        self.btn_delete.setObjectName("btn_delete")
        self.gridLayout_2.addWidget(self.btn_delete, 1, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        UserChange.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(UserChange)
        self.statusbar.setObjectName("statusbar")
        UserChange.setStatusBar(self.statusbar)

        self.retranslateUi(UserChange)
        QtCore.QMetaObject.connectSlotsByName(UserChange)

    def retranslateUi(self, UserChange):
        _translate = QtCore.QCoreApplication.translate
        UserChange.setWindowTitle(_translate("UserChange", "MainWindow"))
        self.lbl_login.setText(_translate("UserChange", "UserName - Qwerty"))
        self.groupBox_2.setTitle(_translate("UserChange", "Blocking"))
        self.btn_unlock.setText(_translate("UserChange", "Unblock"))
        self.btn_lock.setText(_translate("UserChange", "Block"))
        self.btn_time_block.setText(_translate("UserChange", "Block untill"))
        self.groupBox.setTitle(_translate("UserChange", "Change Type"))
        self.comboBox_userType.setItemText(0, _translate("UserChange", "Client"))
        self.comboBox_userType.setItemText(1, _translate("UserChange", "Provider"))
        self.comboBox_userType.setItemText(2, _translate("UserChange", "Admin"))
        self.btn_apply.setText(_translate("UserChange", "Apply"))
        self.btn_delete.setText(_translate("UserChange", "Delete User"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UserChange = QtWidgets.QMainWindow()
    ui = Ui_UserChange()
    ui.setupUi(UserChange)
    UserChange.show()
    sys.exit(app.exec_())
