from PyQt5 import QtWidgets

from QtDesign.py.Error import Ui_DialogError


class ErrorDialog(QtWidgets.QDialog, Ui_DialogError):
    def __init__(self, text):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        self.bt_ok.clicked.connect(self.ok)
        self.plainTextEdit.insertPlainText(text)

    def ok(self):
        self.close()
