# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddManufacturer.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddManufacturer_2(object):
    def setupUi(self, AddManufacturer_2):
        AddManufacturer_2.setObjectName("AddManufacturer_2")
        AddManufacturer_2.resize(255, 96)
        self.centralwidget = QtWidgets.QWidget(AddManufacturer_2)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.edit = QtWidgets.QLineEdit(self.centralwidget)
        self.edit.setEnabled(True)
        self.edit.setObjectName("edit")
        self.gridLayout.addWidget(self.edit, 0, 1, 1, 1)
        self.btn_add = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add.setObjectName("btn_add")
        self.gridLayout.addWidget(self.btn_add, 1, 0, 1, 2)
        AddManufacturer_2.setCentralWidget(self.centralwidget)

        self.retranslateUi(AddManufacturer_2)
        QtCore.QMetaObject.connectSlotsByName(AddManufacturer_2)

    def retranslateUi(self, AddManufacturer_2):
        _translate = QtCore.QCoreApplication.translate
        AddManufacturer_2.setWindowTitle(_translate("AddManufacturer_2", "MainWindow"))
        self.label.setText(_translate("AddManufacturer_2", "Manufacturer"))
        self.btn_add.setText(_translate("AddManufacturer_2", "Add"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddManufacturer_2 = QtWidgets.QMainWindow()
    ui = Ui_AddManufacturer_2()
    ui.setupUi(AddManufacturer_2)
    AddManufacturer_2.show()
    sys.exit(app.exec_())
