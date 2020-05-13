from PyQt5 import QtWidgets

from Forms.AddCategoryForm import AddCategoryForm
from Forms.AddManufacturerForm import AddManufacturerForm
from QtDesign.py.AddNewProduct import Ui_Add_New_Product


class ChangeProductForm(QtWidgets.QMainWindow, Ui_Add_New_Product):
    def __init__(self, db, purchases):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.db = db
        self.purchases = purchases
        self.category_form = None
        self.manufacturer_form = None
        self.categories = self.db.get_categories()
        self.manufacturers = self.db.get_manufacturers()
        self.btn_add.setText('Save Change')
        self.edit_name.setText(self.purchases.product.model)
        self.spinBox_price.setValue(self.purchases.offer.price)
        self.spinBox_amount.setValue(self.purchases.offer.amount)
        self.fill_combobox()
        self.comboBox_manafacturer.setCurrentText(self.purchases.product.manufacturer)
        self.comboBox_category.setCurrentText(self.purchases.product.category)

    def open_add_category_form(self):
        self.category_form = AddCategoryForm(self.db, self)
        self.category_form.show()


    def open_add_manufacturer_form(self):
        self.manufacturer_form = AddManufacturerForm(self.db, self)
        self.manufacturer_form.show()


    def add_new_product(self):
        print(self.edit_name.text())
        print(self.spinBox_price.text())
        print(self.comboBox_category.currentText())
        print(self.comboBox_manafacturer.currentText())
        print(self.spinBox_amount.text())

    def fill_combobox(self):
        self.comboBox_manafacturer.clear()
        self.comboBox_category.clear()
        self.categories = self.db.get_categories()
        self.manufacturers = self.db.get_manufacturers()

        for res in self.categories:
            self.comboBox_category.addItem(res['category'])
        for res in self.manufacturers:
            self.comboBox_manafacturer.addItem(res['manufacturer'])
