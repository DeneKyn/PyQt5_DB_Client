import hashlib

from PyQt5 import QtWidgets

from Forms.AddProviderInfoForm import AddProviderInfoForm
from Forms.ClientStoreForm import ClientStoreForm
from Forms.HistoryForm import HistoryForm
from Forms.StoreAdminForm import StoreAdminForm
from Forms.StoreForm import StoreForm
from QtDesign.py.Profile import Ui_ProfileWindow
from Forms import AdministrationForm


class ProfileForm(QtWidgets.QMainWindow, Ui_ProfileWindow):
    def __init__(self, db, user):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.db = db
        self.user = user
        self.administration_form = None
        self.client_store_form = None
        self.store_form = None
        self.store_admin_form = None
        self.provider_info_form = None
        self.history_form = None
        self.edit_name1.setText(self.user.name1)
        self.edit_name2.setText(self.user.name2)
        self.edit_name3.setText(self.user.name3)
        self.edit_login.setText(self.user.login)
        self.edit_role.setText(self.user.role)
        self.btn_history.clicked.connect(self.open_history_form)
        self.btn_add_provider.clicked.connect(self.open_provider_info_form)
        self.actionSave.triggered.connect(self.on_save)
        self.actionCancel.triggered.connect(self.on_cancel)
        self.Edit.triggered.connect(self.on_edit)
        self.edit(False)
        self.set_warnings()
        self.kek(self.user.role)

    def edit(self, bool_value):
        self.label_password.setVisible(bool_value)
        self.edit_password.setVisible(bool_value)
        self.actionSave.setVisible(bool_value)
        self.actionSave.setVisible(bool_value)
        self.actionCancel.setVisible(bool_value)
        self.edit_name1.setEnabled(bool_value)
        self.label_password.setEnabled(bool_value)
        self.edit_password.setEnabled(bool_value)
        self.edit_name1.setEnabled(bool_value)
        self.edit_name2.setEnabled(bool_value)
        self.edit_name3.setEnabled(bool_value)

    def on_edit(self):
        print(self.user.salt)
        self.edit(True)


    def on_save(self):
        password = self.edit_password.text()
        if not password:
            password = self.user.password
        else:
            password = hashlib.sha512(password.encode('utf-8') + self.user.salt.encode('utf-8')).hexdigest()

        self.db.edit_user(
            self.user.id,
            password,
            self.edit_name1.text(),
            self.edit_name2.text(),
            self.edit_name3.text()
        )
        self.edit(False)

    def on_cancel(self):
        self.edit(False)

    def open_provider_info_form(self):
        self.provider_info_form = AddProviderInfoForm(self.db, self.user)
        self.provider_info_form.show()

    def open_administration_form(self):
        self.administration_form = AdministrationForm.AdministrationForm(self.db, self.user)
        self.administration_form.show()
        self.close()

    def open_store_form(self):
        self.store_form = StoreForm(self.db, self.user)
        self.store_form.show()
        self.close()

    def open_store_admin_Form(self):
        self.store_admin_form = StoreAdminForm(self.db, self.user)
        self.store_admin_form.show()
        self.close()

    def open_client_store_form(self):
        self.client_store_form = ClientStoreForm(self.db, self.user)
        self.client_store_form.show()
        self.close()

    def open_history_form(self):
        self.history_form = HistoryForm(self.db, self.user)
        self.history_form.show()

    def set_warnings(self):
        if self.user.company_name is None:
            self.label_warning.setVisible(True)
            self.label_warning.setText('Missing bank detail information')
            self.label_warning.setStyleSheet('color: red; font-size: 12px')
            self.label_warning_2.setText('and company name')
            self.label_warning_2.setStyleSheet('color: red; font-size: 12px')
        else:
            self.label_warning.setVisible(False)
            self.label_warning_2.setText(f'Company name: \n{self.user.company_name}')
            self.label_warning_2.setStyleSheet('color: black; font-size: 16px')
            self.btn_add_provider.setText('Change')

    def kek(self, role):
        if role == 'Admin':
            self.btn_administration.clicked.connect(self.open_administration_form)
            self.btn_products.clicked.connect(self.open_store_admin_Form)
            self.btn_products.setText('Storage and Providers')
            self.frame_3.setVisible(False)
            self.btn_administration.setVisible(True)
            self.btn_history.setVisible(False)
        elif role == 'Provider':
            print('Provider')
            self.btn_products.clicked.connect(self.open_store_form)
            self.btn_products.setText('Storage')
            self.frame_3.setVisible(True)
            self.btn_administration.setVisible(False)
            self.btn_history.setVisible(False)
        elif role == 'Client':
            self.btn_products.clicked.connect(self.open_client_store_form)
            self.btn_products.setText('Store')
            self.frame_3.setVisible(False)
            self.btn_administration.setVisible(False)
            self.btn_history.setVisible(True)

