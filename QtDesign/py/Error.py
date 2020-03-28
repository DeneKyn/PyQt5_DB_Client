# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Error.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogError(object):
    def setupUi(self, DialogError):
        DialogError.setObjectName("DialogError")
        DialogError.resize(215, 163)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        DialogError.setFont(font)
        DialogError.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.gridLayout = QtWidgets.QGridLayout(DialogError)
        self.gridLayout.setObjectName("gridLayout")
        self.bt_ok = QtWidgets.QPushButton(DialogError)
        self.bt_ok.setObjectName("bt_ok")
        self.gridLayout.addWidget(self.bt_ok, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.lbl_error = QtWidgets.QLabel(DialogError)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lbl_error.setFont(font)
        self.lbl_error.setObjectName("lbl_error")
        self.gridLayout.addWidget(self.lbl_error, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(DialogError)
        self.plainTextEdit.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 1, 0, 1, 1)

        self.retranslateUi(DialogError)
        QtCore.QMetaObject.connectSlotsByName(DialogError)

    def retranslateUi(self, DialogError):
        _translate = QtCore.QCoreApplication.translate
        DialogError.setWindowTitle(_translate("DialogError", "Dialog"))
        self.bt_ok.setText(_translate("DialogError", "Ok"))
        self.lbl_error.setText(_translate("DialogError", "Error"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogError = QtWidgets.QDialog()
    ui = Ui_DialogError()
    ui.setupUi(DialogError)
    DialogError.show()
    sys.exit(app.exec_())
