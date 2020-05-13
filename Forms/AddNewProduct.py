from PyQt5 import QtWidgets

from Forms.AddCategoryForm import AddCategoryForm
from Forms.AddManufacturerForm import AddManufacturerForm
from QtDesign.py.AddNewProduct import Ui_Add_New_Product


class AddNewProductForm(QtWidgets.QMainWindow, Ui_Add_New_Product):
    def __init__(self, db, user):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.db = db
        self.user = user
        self.category_form = None
        self.manufacturer_form = None
        self.categories = self.db.get_categories()
        self.manufacturers = self.db.get_manufacturers()
        self.btn_add.clicked.connect(self.add_new_product)
        self.actionAdd_catecory.triggered.connect(self.open_add_category_form)
        self.actionAdd_manufacturer.triggered.connect(self.open_add_manufacturer_form)
        self.fill_combobox()

    def open_add_category_form(self):
        self.category_form = AddCategoryForm(self.db, self)
        self.category_form.show()


    def open_add_manufacturer_form(self):
        self.manufacturer_form = AddManufacturerForm(self.db, self)
        self.manufacturer_form.show()

    def add_new_product(self):
        self.db.insert_product(
            self.edit_name.text(),
            self.comboBox_category.currentText(),
            self.comboBox_manafacturer.currentText(),
            self.spinBox_amount.text(),
            self.spinBox_price.text(),
            self.user.id
        )
        print(self.edit_name.text())
        print(self.comboBox_category.currentText())
        print(self.comboBox_manafacturer.currentText())
        print(self.spinBox_amount.text())
        print(self.spinBox_price.text())




    def fill_combobox(self):
        self.comboBox_manafacturer.clear()
        self.comboBox_category.clear()
        self.categories = self.db.get_categories()
        self.manufacturers = self.db.get_manufacturers()

        for res in self.categories:
            self.comboBox_category.addItem(res['category'])
        for res in self.manufacturers:
            self.comboBox_manafacturer.addItem(res['manufacturer'])
