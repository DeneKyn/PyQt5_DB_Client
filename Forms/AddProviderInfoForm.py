from PyQt5 import QtWidgets
from QtDesign.py.AddProviderInfo import Ui_AddProviderInfo


class AddProviderInfoForm(QtWidgets.QMainWindow, Ui_AddProviderInfo):
    def __init__(self, db, user):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.db = db
        self.user = user
        self.btn_save.clicked.connect(self.on_save)

    def on_save(self):
        self.db.insert_provider_info(
            self.user.id,
            self.edit_3.text(),
            int(self.edit_1.text()),
            self.edit_2.text()
        )
