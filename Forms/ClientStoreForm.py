from PyQt5 import QtWidgets

from Forms.BuyProductForm import BuyProductForm
from QtDesign.py.ClientProductList import Ui_MainWindow


class ClientStoreForm(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, db, user):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.db = db
        self.user = user
        self.products = self.db.get_product_for_client()
        self.categories = self.db.get_categories()
        self.manufacturers = self.db.get_manufacturers()
        self.sort_type = 0
        self.fill_combobox()
        self.table_fill(self.products)
        self.tableWidget.clicked.connect(self.view_clicked)
        self.pushButton.clicked.connect(self.search_product_for_user)
        self.pushButton_2.clicked.connect(self.sort_product_by_price)
        self.pushButton_3.clicked.connect(self.sort_product_by_sales)
        self.tableWidget.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        self.pushButton_2.setText('Name')
        self.lbl_name2_3.setText('Name')

    def sort_product_by_price(self):
        self.sort_type = 1
        self.search_user()

    def sort_product_by_sales(self):
        self.sort_type = 2
        self.search_user()

    def search_user(self):
        self.products = self.db.get_product_for_client(
            self.edit_name2.text(),
            self.comboBox.currentText(),
            self.comboBox_2.currentText(),
            self.sort_type
        )
        self.table_fill(self.products)

    def search_product_for_user(self):
        self.search_user()

    def table_fill(self, products):
        self.tableWidget.setRowCount(len(products))
        i = 0
        for p in products:

            self.insert_row(i, p.category, p.manufacturer, p.model, p.price, p.offers)
            i = i + 1

    def fill_combobox(self):
        self.comboBox.addItem('All')
        self.comboBox_2.addItem('All')
        for res in self.categories:
            self.comboBox.addItem(res['category'])
        for res in self.manufacturers:
            self.comboBox_2.addItem(res['manufacturer'])

    def insert_row(self, row_id, category, manufacturer, model, price, offers):
        self.tableWidget.setItem(row_id, 0, QtWidgets.QTableWidgetItem(category))
        self.tableWidget.setItem(row_id, 1, QtWidgets.QTableWidgetItem(manufacturer))
        self.tableWidget.setItem(row_id, 2, QtWidgets.QTableWidgetItem(model))
        self.tableWidget.setItem(row_id, 3, QtWidgets.QTableWidgetItem(str(price)))
        self.tableWidget.setItem(row_id, 4, QtWidgets.QTableWidgetItem(str(offers)))

    def view_clicked(self):
        indexes = self.tableWidget.selectionModel().selectedRows()
        id_row = indexes[0].row()
        print(self.products[id_row])
        print(self.products[id_row].id)
        self.buy_product_form = BuyProductForm(self.db, self.user, self.products[id_row])
        self.buy_product_form.show()


