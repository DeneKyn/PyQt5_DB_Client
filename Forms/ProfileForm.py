from PyQt5 import QtWidgets
from QtDesign.py.Profile import Ui_ProfileWindow
from Forms import AdministrationForm


class ProfileForm(QtWidgets.QMainWindow, Ui_ProfileWindow):
    def __init__(self, db, user):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.db = db
        self.user = user
        self.edit_name1.setText(self.user.name1)
        self.edit_name2.setText(self.user.name2)
        self.edit_name3.setText(self.user.name3)
        self.edit_login.setText(self.user.login)
        self.edit_role.setText(self.user.role)
        self.btn_administration.clicked.connect(self.open_administration_form)

    def open_administration_form(self):
        self.administration_form = AdministrationForm.AdministrationForm(self.db, self.user)
        self.administration_form.show()
        self.close()

