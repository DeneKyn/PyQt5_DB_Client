# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddProviderInfo.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddProviderInfo(object):
    def setupUi(self, AddProviderInfo):
        AddProviderInfo.setObjectName("AddProviderInfo")
        AddProviderInfo.resize(326, 229)
        self.centralwidget = QtWidgets.QWidget(AddProviderInfo)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setContentsMargins(9, 9, 9, 9)
        self.gridLayout.setHorizontalSpacing(25)
        self.gridLayout.setObjectName("gridLayout")
        self.label_login = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_login.setFont(font)
        self.label_login.setObjectName("label_login")
        self.gridLayout.addWidget(self.label_login, 0, 0, 1, 1)
        self.edit_1 = QtWidgets.QLineEdit(self.frame)
        self.edit_1.setEnabled(True)
        self.edit_1.setObjectName("edit_1")
        self.gridLayout.addWidget(self.edit_1, 0, 1, 1, 1)
        self.label_role = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_role.setFont(font)
        self.label_role.setObjectName("label_role")
        self.gridLayout.addWidget(self.label_role, 1, 0, 1, 1)
        self.edit_2 = QtWidgets.QLineEdit(self.frame)
        self.edit_2.setEnabled(True)
        self.edit_2.setObjectName("edit_2")
        self.gridLayout.addWidget(self.edit_2, 1, 1, 1, 1)
        self.label_password = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_password.setFont(font)
        self.label_password.setObjectName("label_password")
        self.gridLayout.addWidget(self.label_password, 2, 0, 1, 1)
        self.edit_3 = QtWidgets.QLineEdit(self.frame)
        self.edit_3.setEnabled(True)
        self.edit_3.setObjectName("edit_3")
        self.gridLayout.addWidget(self.edit_3, 2, 1, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        self.btn_save = QtWidgets.QPushButton(self.centralwidget)
        self.btn_save.setObjectName("btn_save")
        self.verticalLayout.addWidget(self.btn_save, 0, QtCore.Qt.AlignHCenter)
        AddProviderInfo.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AddProviderInfo)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 326, 21))
        self.menubar.setObjectName("menubar")
        AddProviderInfo.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AddProviderInfo)
        self.statusbar.setObjectName("statusbar")
        AddProviderInfo.setStatusBar(self.statusbar)

        self.retranslateUi(AddProviderInfo)
        QtCore.QMetaObject.connectSlotsByName(AddProviderInfo)

    def retranslateUi(self, AddProviderInfo):
        _translate = QtCore.QCoreApplication.translate
        AddProviderInfo.setWindowTitle(_translate("AddProviderInfo", "MainWindow"))
        self.label_login.setText(_translate("AddProviderInfo", "Payer account\n"
"number"))
        self.label_role.setText(_translate("AddProviderInfo", "Bank branch"))
        self.label_password.setText(_translate("AddProviderInfo", "Company name"))
        self.btn_save.setText(_translate("AddProviderInfo", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddProviderInfo = QtWidgets.QMainWindow()
    ui = Ui_AddProviderInfo()
    ui.setupUi(AddProviderInfo)
    AddProviderInfo.show()
    sys.exit(app.exec_())
