from PyQt5 import QtWidgets

from QtDesign.py.History import Ui_History


class HistoryForm(QtWidgets.QMainWindow, Ui_History):
    def __init__(self, db, user):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.db = db
        self.user = user
        self.label_name.setText(f"{self.user.login} History")
        self.purchases = self.db.get_user_purchases(self.user.id)
        print(self.purchases)
        self.fill_list()

    def fill_list(self):
        for p in self.purchases:
            self.list_history.addItem(f"{p.product.category} {p.product.manufacturer} {p.product.model} \t"
                                      f"Provider: {p.offer.company_name} Amount: {p.offer.amount}"
                                      f" Total Price: {p.offer.price}")

