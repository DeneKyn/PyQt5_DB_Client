# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Administration.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AdministrationWindow(object):
    def setupUi(self, AdministrationWindow):
        AdministrationWindow.setObjectName("AdministrationWindow")
        AdministrationWindow.setEnabled(True)
        AdministrationWindow.resize(644, 475)
        AdministrationWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(AdministrationWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.BoxFullName = QtWidgets.QGroupBox(self.centralwidget)
        self.BoxFullName.setObjectName("BoxFullName")
        self.gridLayout = QtWidgets.QGridLayout(self.BoxFullName)
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_name2 = QtWidgets.QLabel(self.BoxFullName)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_name2.setFont(font)
        self.lbl_name2.setObjectName("lbl_name2")
        self.gridLayout.addWidget(self.lbl_name2, 0, 0, 1, 1)
        self.edit_name2 = QtWidgets.QLineEdit(self.BoxFullName)
        self.edit_name2.setObjectName("edit_name2")
        self.gridLayout.addWidget(self.edit_name2, 0, 1, 1, 1)
        self.lbl_name1 = QtWidgets.QLabel(self.BoxFullName)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_name1.setFont(font)
        self.lbl_name1.setObjectName("lbl_name1")
        self.gridLayout.addWidget(self.lbl_name1, 1, 0, 1, 1)
        self.edit_name1 = QtWidgets.QLineEdit(self.BoxFullName)
        self.edit_name1.setObjectName("edit_name1")
        self.gridLayout.addWidget(self.edit_name1, 1, 1, 1, 1)
        self.lbl_name3 = QtWidgets.QLabel(self.BoxFullName)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_name3.setFont(font)
        self.lbl_name3.setObjectName("lbl_name3")
        self.gridLayout.addWidget(self.lbl_name3, 2, 0, 1, 1)
        self.edit_name3 = QtWidgets.QLineEdit(self.BoxFullName)
        self.edit_name3.setObjectName("edit_name3")
        self.gridLayout.addWidget(self.edit_name3, 2, 1, 1, 1)
        self.horizontalLayout.addWidget(self.BoxFullName)
        self.BoxUserType = QtWidgets.QGroupBox(self.centralwidget)
        self.BoxUserType.setObjectName("BoxUserType")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.BoxUserType)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.rBtn_admin = QtWidgets.QRadioButton(self.BoxUserType)
        self.rBtn_admin.setObjectName("rBtn_admin")
        self.gridLayout_3.addWidget(self.rBtn_admin, 2, 0, 1, 1)
        self.rBtn_client = QtWidgets.QRadioButton(self.BoxUserType)
        self.rBtn_client.setObjectName("rBtn_client")
        self.gridLayout_3.addWidget(self.rBtn_client, 0, 0, 1, 1)
        self.rBtn_provider = QtWidgets.QRadioButton(self.BoxUserType)
        self.rBtn_provider.setObjectName("rBtn_provider")
        self.gridLayout_3.addWidget(self.rBtn_provider, 1, 0, 1, 1)
        self.horizontalLayout.addWidget(self.BoxUserType)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.rBtn_Active = QtWidgets.QRadioButton(self.groupBox)
        self.rBtn_Active.setObjectName("rBtn_Active")
        self.verticalLayout.addWidget(self.rBtn_Active)
        self.rBtn_Blocked = QtWidgets.QRadioButton(self.groupBox)
        self.rBtn_Blocked.setObjectName("rBtn_Blocked")
        self.verticalLayout.addWidget(self.rBtn_Blocked)
        self.horizontalLayout.addWidget(self.groupBox)
        self.btn_find = QtWidgets.QPushButton(self.centralwidget)
        self.btn_find.setObjectName("btn_find")
        self.horizontalLayout.addWidget(self.btn_find)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        AdministrationWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AdministrationWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 644, 21))
        self.menubar.setObjectName("menubar")
        AdministrationWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AdministrationWindow)
        self.statusbar.setObjectName("statusbar")
        AdministrationWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AdministrationWindow)
        QtCore.QMetaObject.connectSlotsByName(AdministrationWindow)

    def retranslateUi(self, AdministrationWindow):
        _translate = QtCore.QCoreApplication.translate
        AdministrationWindow.setWindowTitle(_translate("AdministrationWindow", "Administration"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("AdministrationWindow", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("AdministrationWindow", "2"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("AdministrationWindow", "UserName"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("AdministrationWindow", "Role"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("AdministrationWindow", "First Name"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("AdministrationWindow", "Patronymic "))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("AdministrationWindow", "Lsat Name"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("AdministrationWindow", "Status"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.BoxFullName.setTitle(_translate("AdministrationWindow", "Full Name"))
        self.lbl_name2.setText(_translate("AdministrationWindow", "First name"))
        self.lbl_name1.setText(_translate("AdministrationWindow", "Last name"))
        self.lbl_name3.setText(_translate("AdministrationWindow", "Patronymic"))
        self.BoxUserType.setTitle(_translate("AdministrationWindow", "User Type"))
        self.rBtn_admin.setText(_translate("AdministrationWindow", "Admin"))
        self.rBtn_client.setText(_translate("AdministrationWindow", "Client"))
        self.rBtn_provider.setText(_translate("AdministrationWindow", "Provider"))
        self.groupBox.setTitle(_translate("AdministrationWindow", "User Status"))
        self.rBtn_Active.setText(_translate("AdministrationWindow", "Active"))
        self.rBtn_Blocked.setText(_translate("AdministrationWindow", "Blocked"))
        self.btn_find.setText(_translate("AdministrationWindow", "Find"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AdministrationWindow = QtWidgets.QMainWindow()
    ui = Ui_AdministrationWindow()
    ui.setupUi(AdministrationWindow)
    AdministrationWindow.show()
    sys.exit(app.exec_())
