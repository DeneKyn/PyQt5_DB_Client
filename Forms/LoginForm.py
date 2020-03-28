import hashlib
import os

from PyQt5 import QtWidgets

from Forms.ErrorDialog import ErrorDialog
from QtDesign.py.Login import Ui_LoginWindow

from Forms import RegisterForm, ProfileForm


class LoginWindow(QtWidgets.QMainWindow, Ui_LoginWindow):
    def __init__(self, db):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.db = db
        self.btn_register.clicked.connect(self.open_registration_form)
        self.btn_login.clicked.connect(self.open_profile_form)

    def open_registration_form(self):
        self.register_form = RegisterForm.RegisterForm(self.db)
        self.register_form.show()
        self.close()

    def open_profile_form(self):
        try:
            user = self.db.login_user(
                self.edit_login.text(),
                self.edit_password.text(),
            )
            self.profile_form = ProfileForm.ProfileForm(self.db, user)
            self.profile_form.show()
            self.close()

        except ValueError as err:
            s = str(err)
            self.error = ErrorDialog(s)
            self.error.show()

