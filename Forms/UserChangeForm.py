from PyQt5 import QtWidgets
from PyQt5.QtCore import QDateTime
from QtDesign.py.UserChange import Ui_UserChange


class UserChangeForm(QtWidgets.QMainWindow, Ui_UserChange):
    def __init__(self, db, login, parent):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.db = db
        self.login = login
        self.parent = parent
        self.lbl_login.setText(f"UserName - {login}")
        self.dateTimeEdit.setDateTime(QDateTime.currentDateTime())
        self.btn_apply.clicked.connect(self.update_user_type)
        self.btn_lock.clicked.connect(self.block_forever)
        self.btn_unlock.clicked.connect(self.unlock)
        self.btn_time_block.clicked.connect(self.block_temporary)
        self.btn_delete.clicked.connect(self.delete)

    def update_user_type(self):
        user_type = self.comboBox_userType.currentText()
        self.db.update_user_type(self.login, user_type)
        self.parent.filter_users()

    def block_forever(self):
        self.db.block_user_forever(self.login)
        self.parent.filter_users()

    def unlock(self):
        self.db.unlock_user(self.login)
        self.parent.filter_users()

    def block_temporary(self):
        block_end = self.dateTimeEdit.dateTime().toUTC()
        sec = abs(block_end.secsTo(QDateTime.currentDateTime()))
        self.db.block_user_temporary(self.login, sec)
        self.parent.filter_users()

    def delete(self):
        self.db.delete_user(self.login)
        self.parent.filter_users()
        self.close()
