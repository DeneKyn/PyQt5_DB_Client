# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'History.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_History(object):
    def setupUi(self, History):
        History.setObjectName("History")
        History.resize(569, 284)
        self.centralwidget = QtWidgets.QWidget(History)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_name = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_name.setFont(font)
        self.label_name.setObjectName("label_name")
        self.verticalLayout.addWidget(self.label_name, 0, QtCore.Qt.AlignHCenter)
        self.list_history = QtWidgets.QListWidget(self.centralwidget)
        self.list_history.setObjectName("list_history")
        self.verticalLayout.addWidget(self.list_history)
        History.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(History)
        self.statusbar.setObjectName("statusbar")
        History.setStatusBar(self.statusbar)

        self.retranslateUi(History)
        QtCore.QMetaObject.connectSlotsByName(History)

    def retranslateUi(self, History):
        _translate = QtCore.QCoreApplication.translate
        History.setWindowTitle(_translate("History", "MainWindow"))
        self.label_name.setText(_translate("History", "UserName History"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    History = QtWidgets.QMainWindow()
    ui = Ui_History()
    ui.setupUi(History)
    History.show()
    sys.exit(app.exec_())
