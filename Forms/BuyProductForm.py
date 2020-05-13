from PyQt5 import QtWidgets
from pymysql import IntegrityError, MySQLError

from Forms.ErrorDialog import ErrorDialog
from QtDesign.py.BuyProduct import Ui_BuyProduct


class BuyProductForm(QtWidgets.QMainWindow, Ui_BuyProduct):
    def __init__(self, db, user, product):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.db = db
        self.user = user
        self.product = product
        self.selected_id = 0
        self.offers = self.db.get_product_offers(self.product.id)
        self.label_name.setText(f"{self.product.category} - {self.product.manufacturer} - {self.product.model}")
        self.btn_buy.clicked.connect(self.buy_product)
        self.fill_list()
        self.list_products.itemSelectionChanged.connect(self.selection_changed)
        print(product.id)

    def selection_changed(self):
        self.selected_id = self.list_products.currentRow()
        self.label_provider.setText(
            self.offers[self.selected_id].company_name
        )

    def buy_product(self):
        try:
            self.db.buy_product(self.product, self.spinBox_amount.text(), self.user.id)
            self.close()
        except MySQLError as err:
            if err.args[0] == 1690:
                s = "Not enought product on storage"
                self.error_from = ErrorDialog(s)
                self.error_from.show()

    def fill_list(self):
        for o in self.offers:
            self.list_products.addItem(f"{o.company_name} - {o.price}")
