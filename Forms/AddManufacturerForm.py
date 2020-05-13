from PyQt5 import QtWidgets
from QtDesign.py.AddManufacturer import Ui_AddManufacturer_2


class AddManufacturerForm(QtWidgets.QMainWindow, Ui_AddManufacturer_2):
    def __init__(self, db, add_new_product):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.db = db
        self.add_new_product = add_new_product
        self.btn_add.clicked.connect(self.add_manufacturer)

    def add_manufacturer(self):
        self.db.insert_manufacturer(self.edit.text())
        self.add_new_product.fill_combobox()
        self.close()
