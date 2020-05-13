from PyQt5 import QtWidgets
from QtDesign.py.StoreAdmin import Ui_MainWindow


class StoreAdminForm(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, db, user):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.db = db
        self.user = user
        self.offers = None
        self.tableWidget.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        self.tableWidget_2.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        self.tableWidget_2.clicked.connect(self.view_clicked)
        self.selected_id = 0
        self.table_fill()
        self.fill_table_providers()
        self.rBtn_sales.clicked.connect(self.table_fill)
        self.rBtn_products.clicked.connect(self.table_fill)
        self.rBtn_sort_products.clicked.connect(self.fill_table_providers)
        self.rBtn_sort_sales.clicked.connect(self.fill_table_providers)


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
        is_products = self.rBtn_products.isChecked()
        is_all = True if self.selected_id == 0 else False

        if is_products:
            self.purchases = self.db.get_provider_products(self.selected_id)
        elif not is_products:
            self.purchases = self.db.get_provider_sales(self.selected_id)

        self.tableWidget.setRowCount(len(self.purchases))
        i = 0
        for p in self.purchases:
            self.insert_row(i, p, is_all, is_products)
            i = i + 1

    def insert_row_provider(self, row_id, o):

        self.tableWidget_2.setItem(row_id, 0, QtWidgets.QTableWidgetItem(o.company_name))
        self.tableWidget_2.setItem(row_id, 1, QtWidgets.QTableWidgetItem(str(o.sales_amount)))
        self.tableWidget_2.setItem(row_id, 2, QtWidgets.QTableWidgetItem(str(o.storage_amount)))

    def fill_table_providers(self):
        sort_type = 0
        if self.rBtn_sort_sales.isChecked():
            sort_type = 1
        elif self.rBtn_sort_products:
            sort_type = 2

        self.offers = self.db.get_providers(sort_type)
        self.tableWidget_2.setRowCount(len(self.offers))


        self.tableWidget_2.setColumnCount(3)
        self.tableWidget_2.setHorizontalHeaderLabels(('Provider', 'Sales', 'Products\nin stock'))
        header = self.tableWidget_2.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        i = 0
        for o in self.offers:
            self.insert_row_provider(i, o)
            i = i + 1

    def view_clicked(self):
        indexes = self.tableWidget_2.selectionModel().selectedRows()
        id_row = indexes[0].row()
        self.selected_id = self.offers[id_row].id
        self.table_fill()


