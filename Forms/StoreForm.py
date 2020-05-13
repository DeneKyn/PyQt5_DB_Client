from PyQt5 import QtWidgets

from Forms.AddNewProduct import AddNewProductForm
from Forms.ChangeProduct import ChangeProductForm
from QtDesign.py.Store import Ui_MainWindow


class StoreForm(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, db, user):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.db = db
        self.user = user
        self.purchases = None
        self.new_product_form = None
        self.change_product_form = None
        self.btn_add.clicked.connect(self.open_new_product_form)
        self.rBtn_my.clicked.connect(self.table_fill)
        self.rBtn_all.clicked.connect(self.table_fill)
        self.rBtn_products.clicked.connect(self.table_fill)
        self.rBtn_sales.clicked.connect(self.table_fill)
        self.tableWidget.clicked.connect(self.view_clicked)
        self.tableWidget.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        self.table_fill()

    def open_new_product_form(self):
        self.new_product_form = AddNewProductForm(self.db, self.user)
        self.new_product_form.show()

    def insert_row(self, row_id, p, is_all, is_products):
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)

        if is_all and is_products:
            self.tableWidget.setColumnCount(5)
            self.tableWidget.setHorizontalHeaderLabels(('Date', 'Provider', 'Product', 'Amount', 'Price'))
            header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)

            self.tableWidget.setItem(row_id, 0, QtWidgets.QTableWidgetItem(str(p.product.date_to_storage)))
            self.tableWidget.setItem(row_id, 1, QtWidgets.QTableWidgetItem(str(p.offer.company_name)))
            self.tableWidget.setItem(row_id, 2, QtWidgets.QTableWidgetItem(
                f"{p.product.category} {p.product.manufacturer} {p.product.model}"))
            self.tableWidget.setItem(row_id, 3, QtWidgets.QTableWidgetItem(str(p.offer.amount)))
            self.tableWidget.setItem(row_id, 4, QtWidgets.QTableWidgetItem(str(p.offer.price)))

        elif not is_all and is_products:
            self.tableWidget.setColumnCount(4)
            self.tableWidget.setHorizontalHeaderLabels(('Date', 'Product', 'Amount', 'Price'))
            header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)

            self.tableWidget.setItem(row_id, 0, QtWidgets.QTableWidgetItem(str(p.product.date_to_storage)))
            self.tableWidget.setItem(row_id, 1, QtWidgets.QTableWidgetItem(
                f"{p.product.category} {p.product.manufacturer} {p.product.model}"))
            self.tableWidget.setItem(row_id, 2, QtWidgets.QTableWidgetItem(str(p.offer.amount)))
            self.tableWidget.setItem(row_id, 3, QtWidgets.QTableWidgetItem(str(p.offer.price)))

        elif is_all and not is_products:
            self.tableWidget.setColumnCount(6)
            self.tableWidget.setHorizontalHeaderLabels(('Login', 'Date', 'Provider' 'Product', 'Amount', 'Price'))
            header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)

            self.tableWidget.setItem(row_id, 0, QtWidgets.QTableWidgetItem(str(p.login)))
            self.tableWidget.setItem(row_id, 1, QtWidgets.QTableWidgetItem(str(p.date_of_sale)))
            self.tableWidget.setItem(row_id, 2, QtWidgets.QTableWidgetItem(str(p.offer.company_name)))
            self.tableWidget.setItem(row_id, 3, QtWidgets.QTableWidgetItem(
                f"{p.product.category} {p.product.manufacturer} {p.product.model}"))
            self.tableWidget.setItem(row_id, 4, QtWidgets.QTableWidgetItem(str(p.offer.amount)))
            self.tableWidget.setItem(row_id, 5, QtWidgets.QTableWidgetItem(str(p.offer.price)))

        elif not is_all and not is_products:
            self.tableWidget.setColumnCount(5)
            self.tableWidget.setHorizontalHeaderLabels(('Login', 'Date', 'Product', 'Amount', 'Price'))
            header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)

            self.tableWidget.setItem(row_id, 0, QtWidgets.QTableWidgetItem(str(p.login)))
            self.tableWidget.setItem(row_id, 1, QtWidgets.QTableWidgetItem(str(p.date_of_sale)))
            self.tableWidget.setItem(row_id, 2, QtWidgets.QTableWidgetItem(
                f"{p.product.category} {p.product.manufacturer} {p.product.model}"))
            self.tableWidget.setItem(row_id, 3, QtWidgets.QTableWidgetItem(str(p.offer.amount)))
            self.tableWidget.setItem(row_id, 4, QtWidgets.QTableWidgetItem(str(p.offer.price)))

    def table_fill(self):
        is_all = self.rBtn_all.isChecked()
        is_products = self.rBtn_products.isChecked()

        if is_all and is_products:
            self.purchases = self.db.get_provider_products(0)
        elif not is_all and is_products:
            self.purchases = self.db.get_provider_products(self.user.id)
        elif is_all and not is_products:
            self.purchases = self.db.get_provider_sales(0)
        elif not is_all and not is_products:
            self.purchases = self.db.get_provider_sales(self.user.id)

        self.tableWidget.setRowCount(len(self.purchases))
        i = 0
        for p in self.purchases:
            self.insert_row(i, p, is_all, is_products)
            i = i + 1

    def view_clicked(self):
        indexes = self.tableWidget.selectionModel().selectedRows()
        id_row = indexes[0].row()
        kek = self.purchases[id_row].product
        self.change_product_form = ChangeProductForm(self.db, self.purchases[id_row])
        self.change_product_form.show()
        print(id_row)
        print(indexes)
