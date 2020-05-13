# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BuyProduct.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BuyProduct(object):
    def setupUi(self, BuyProduct):
        BuyProduct.setObjectName("BuyProduct")
        BuyProduct.resize(545, 153)
        BuyProduct.setMinimumSize(QtCore.QSize(545, 153))
        BuyProduct.setMaximumSize(QtCore.QSize(545, 153))
        self.centralwidget = QtWidgets.QWidget(BuyProduct)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_name = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_name.setFont(font)
        self.label_name.setObjectName("label_name")
        self.gridLayout_2.addWidget(self.label_name, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.list_products = QtWidgets.QListWidget(self.centralwidget)
        self.list_products.setObjectName("list_products")
        self.gridLayout_2.addWidget(self.list_products, 1, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.label_provider = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_provider.setFont(font)
        self.label_provider.setObjectName("label_provider")
        self.gridLayout.addWidget(self.label_provider, 0, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.label_amount = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_amount.setFont(font)
        self.label_amount.setObjectName("label_amount")
        self.gridLayout.addWidget(self.label_amount, 1, 0, 1, 1)
        self.spinBox_amount = QtWidgets.QSpinBox(self.frame)
        self.spinBox_amount.setObjectName("spinBox_amount")
        self.gridLayout.addWidget(self.spinBox_amount, 1, 1, 1, 1)
        self.btn_buy = QtWidgets.QPushButton(self.frame)
        self.btn_buy.setMinimumSize(QtCore.QSize(101, 41))
        self.btn_buy.setObjectName("btn_buy")
        self.gridLayout.addWidget(self.btn_buy, 2, 0, 1, 2)
        self.gridLayout_2.addWidget(self.frame, 0, 1, 2, 1)
        BuyProduct.setCentralWidget(self.centralwidget)

        self.retranslateUi(BuyProduct)
        QtCore.QMetaObject.connectSlotsByName(BuyProduct)

    def retranslateUi(self, BuyProduct):
        _translate = QtCore.QCoreApplication.translate
        BuyProduct.setWindowTitle(_translate("BuyProduct", "MainWindow"))
        self.label_name.setText(_translate("BuyProduct", "Category - Manufacturer - Name"))
        self.label_provider.setText(_translate("BuyProduct", "Provider"))
        self.label_amount.setText(_translate("BuyProduct", "Amount"))
        self.btn_buy.setText(_translate("BuyProduct", "Buy"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BuyProduct = QtWidgets.QMainWindow()
    ui = Ui_BuyProduct()
    ui.setupUi(BuyProduct)
    BuyProduct.show()
    sys.exit(app.exec_())
