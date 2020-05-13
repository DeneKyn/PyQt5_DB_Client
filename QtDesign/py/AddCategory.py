# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddCategory.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddCategory(object):
    def setupUi(self, AddCategory):
        AddCategory.setObjectName("AddCategory")
        AddCategory.resize(255, 97)
        self.centralwidget = QtWidgets.QWidget(AddCategory)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.lab = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lab.setFont(font)
        self.lab.setObjectName("lab")
        self.gridLayout.addWidget(self.lab, 0, 0, 1, 1)
        self.edit = QtWidgets.QLineEdit(self.centralwidget)
        self.edit.setEnabled(True)
        self.edit.setObjectName("edit")
        self.gridLayout.addWidget(self.edit, 0, 1, 1, 1)
        self.btn_add = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add.setObjectName("btn_add")
        self.gridLayout.addWidget(self.btn_add, 1, 0, 1, 2)
        AddCategory.setCentralWidget(self.centralwidget)

        self.retranslateUi(AddCategory)
        QtCore.QMetaObject.connectSlotsByName(AddCategory)

    def retranslateUi(self, AddCategory):
        _translate = QtCore.QCoreApplication.translate
        AddCategory.setWindowTitle(_translate("AddCategory", "MainWindow"))
        self.lab.setText(_translate("AddCategory", "Category"))
        self.btn_add.setText(_translate("AddCategory", "Add"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddCategory = QtWidgets.QMainWindow()
    ui = Ui_AddCategory()
    ui.setupUi(AddCategory)
    AddCategory.show()
    sys.exit(app.exec_())
