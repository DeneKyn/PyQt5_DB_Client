from PyQt5 import QtWidgets
from QtDesign.py.AddCategory import Ui_AddCategory


class AddCategoryForm(QtWidgets.QMainWindow, Ui_AddCategory):
    def __init__(self, db, add_new_product):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.db = db
        self.add_new_product = add_new_product
        self.btn_add.clicked.connect(self.add_category)

    def add_category(self):
        self.db.insert_category(self.edit.text())
        self.add_new_product.fill_combobox()
        self.close()
