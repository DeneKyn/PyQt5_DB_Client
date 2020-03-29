from PyQt5 import QtWidgets
from Forms import LoginForm
from Models.UserType import UserType
from QtDesign.py.Register import Ui_MainWindow


class RegisterForm(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, db):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.db = db
        self.login_form = None
        self.btn_register.clicked.connect(self.register)

    def register(self):
        self.db.create_user(
            self.edit_login.text(),
            self.edit_password.text(),
            self.checked_radio_btn(),
            self.edit_name1.text(),
            self.edit_name2.text(),
            self.edit_name3.text()
        )
        self.login_form = LoginForm.LoginWindow(self.db)
        self.login_form.show()
        self.close()

    def checked_radio_btn(self):
        if self.rBtn_admin.isChecked():
            return UserType.Admin.value
        elif self.rBtn_client.isChecked():
            return UserType.Client.value
        elif self.rBtn_provider.isChecked():
            return UserType.Provider.value
