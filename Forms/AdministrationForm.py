from PyQt5 import QtWidgets

from Forms.ErrorDialog import ErrorDialog
from Forms.UserChangeForm import UserChangeForm
from Models.UserStatus import UserStatus
from Models.UserType import UserType
from QtDesign.py.Administration import Ui_AdministrationWindow


class AdministrationForm(QtWidgets.QMainWindow, Ui_AdministrationWindow):
    def __init__(self, db, user):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.db = db
        self.user = user
        self.error_form = None
        self.user_change_form = None
        self.users = self.db.get_search_users()
        self.table_fill(self.users)
        self.btn_find.clicked.connect(self.filter_users)
        self.tableWidget.clicked.connect(self.view_clicked)
        self.btn_undo.clicked.connect(self.undo)
        self.tableWidget.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)

    def undo(self):
        try:
            self.db.backup_user()
            self.filter_users()
        except ValueError as err:
            s = str(err)
            self.error_form = ErrorDialog(s)
            self.error_form.show()

    def table_fill(self, users):
        self.tableWidget.setRowCount(len(users))
        i = 0
        for user in users:
            self.insert_row(i, user.login, user.role, user.status, user.name1, user.name2, user.name3)
            i = i + 1

    def filter_users(self):
        self.users = self.get_filter_users()
        self.table_fill(self.users)

    def get_filter_users(self):
        users = self.db.get_search_users(
            self.get_user_status(),
            self.get_user_type(),
            self.edit_name1.text(),
            self.edit_name2.text(),
            self.edit_name3.text()
        )
        return users

    def insert_row(self, row_id, username, role, status, name1, name2, name3):
        self.tableWidget.setItem(row_id, 0, QtWidgets.QTableWidgetItem(username))
        self.tableWidget.setItem(row_id, 1, QtWidgets.QTableWidgetItem(role))
        self.tableWidget.setItem(row_id, 2, QtWidgets.QTableWidgetItem(name1))
        self.tableWidget.setItem(row_id, 3, QtWidgets.QTableWidgetItem(name2))
        self.tableWidget.setItem(row_id, 4, QtWidgets.QTableWidgetItem(name3))
        self.tableWidget.setItem(row_id, 5, QtWidgets.QTableWidgetItem(status))

    def view_clicked(self):
        indexes = self.tableWidget.selectionModel().selectedRows()
        id_row = indexes[0].row()
        login = self.tableWidget.item(id_row, 0).text()
        self.user_change_form = UserChangeForm(self.db, login, self)
        self.user_change_form.show()

    def get_user_type(self):
        if self.rBtn_admin.isChecked():
            return UserType.Admin.value
        elif self.rBtn_client.isChecked():
            return UserType.Client.value
        elif self.rBtn_provider.isChecked():
            return UserType.Provider.value

    def get_user_status(self):
        if self.rBtn_Active.isChecked():
            return UserStatus.Active.value
        elif self.rBtn_Blocked.isChecked():
            return UserStatus.Blocked.value
