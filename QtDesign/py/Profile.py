# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Profile.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ProfileWindow(object):
    def setupUi(self, ProfileWindow):
        ProfileWindow.setObjectName("ProfileWindow")
        ProfileWindow.resize(263, 434)
        ProfileWindow.setMaximumSize(QtCore.QSize(272, 434))
        self.centralwidget = QtWidgets.QWidget(ProfileWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMaximumSize(QtCore.QSize(237, 101))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_login = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_login.setFont(font)
        self.label_login.setObjectName("label_login")
        self.gridLayout_2.addWidget(self.label_login, 0, 0, 1, 1)
        self.edit_login = QtWidgets.QLineEdit(self.frame_2)
        self.edit_login.setEnabled(False)
        self.edit_login.setObjectName("edit_login")
        self.gridLayout_2.addWidget(self.edit_login, 0, 1, 1, 1)
        self.label_role = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_role.setFont(font)
        self.label_role.setObjectName("label_role")
        self.gridLayout_2.addWidget(self.label_role, 1, 0, 1, 1)
        self.edit_role = QtWidgets.QLineEdit(self.frame_2)
        self.edit_role.setEnabled(False)
        self.edit_role.setObjectName("edit_role")
        self.gridLayout_2.addWidget(self.edit_role, 1, 1, 1, 1)
        self.label_password = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_password.setFont(font)
        self.label_password.setObjectName("label_password")
        self.gridLayout_2.addWidget(self.label_password, 2, 0, 1, 1)
        self.edit_password = QtWidgets.QLineEdit(self.frame_2)
        self.edit_password.setEnabled(False)
        self.edit_password.setObjectName("edit_password")
        self.gridLayout_2.addWidget(self.edit_password, 2, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMaximumSize(QtCore.QSize(251, 101))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_name2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_name2.setFont(font)
        self.lbl_name2.setObjectName("lbl_name2")
        self.gridLayout.addWidget(self.lbl_name2, 0, 0, 1, 1)
        self.edit_name2 = QtWidgets.QLineEdit(self.frame)
        self.edit_name2.setEnabled(False)
        self.edit_name2.setObjectName("edit_name2")
        self.gridLayout.addWidget(self.edit_name2, 0, 1, 1, 1)
        self.lbl_name1 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_name1.setFont(font)
        self.lbl_name1.setObjectName("lbl_name1")
        self.gridLayout.addWidget(self.lbl_name1, 1, 0, 1, 1)
        self.edit_name1 = QtWidgets.QLineEdit(self.frame)
        self.edit_name1.setEnabled(False)
        self.edit_name1.setObjectName("edit_name1")
        self.gridLayout.addWidget(self.edit_name1, 1, 1, 1, 1)
        self.lbl_name3 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_name3.setFont(font)
        self.lbl_name3.setObjectName("lbl_name3")
        self.gridLayout.addWidget(self.lbl_name3, 2, 0, 1, 1)
        self.edit_name3 = QtWidgets.QLineEdit(self.frame)
        self.edit_name3.setEnabled(False)
        self.edit_name3.setObjectName("edit_name3")
        self.gridLayout.addWidget(self.edit_name3, 2, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.frame)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setMaximumSize(QtCore.QSize(245, 61))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_warning = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_warning.setFont(font)
        self.label_warning.setObjectName("label_warning")
        self.gridLayout_3.addWidget(self.label_warning, 0, 0, 1, 1)
        self.btn_add_provider = QtWidgets.QPushButton(self.frame_3)
        self.btn_add_provider.setMinimumSize(QtCore.QSize(75, 41))
        self.btn_add_provider.setObjectName("btn_add_provider")
        self.gridLayout_3.addWidget(self.btn_add_provider, 0, 1, 2, 1)
        self.label_warning_2 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_warning_2.setFont(font)
        self.label_warning_2.setObjectName("label_warning_2")
        self.gridLayout_3.addWidget(self.label_warning_2, 1, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setMaximumSize(QtCore.QSize(241, 101))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_administration = QtWidgets.QPushButton(self.frame_4)
        self.btn_administration.setObjectName("btn_administration")
        self.verticalLayout.addWidget(self.btn_administration)
        self.btn_history = QtWidgets.QPushButton(self.frame_4)
        self.btn_history.setObjectName("btn_history")
        self.verticalLayout.addWidget(self.btn_history)
        self.btn_products = QtWidgets.QPushButton(self.frame_4)
        self.btn_products.setObjectName("btn_products")
        self.verticalLayout.addWidget(self.btn_products)
        self.verticalLayout_2.addWidget(self.frame_4)
        ProfileWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtWidgets.QToolBar(ProfileWindow)
        self.toolBar.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.toolBar.setMovable(False)
        self.toolBar.setObjectName("toolBar")
        ProfileWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.Edit = QtWidgets.QAction(ProfileWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/pencil.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Edit.setIcon(icon)
        self.Edit.setObjectName("Edit")
        self.actionSave = QtWidgets.QAction(ProfileWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/ok.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon1)
        self.actionSave.setObjectName("actionSave")
        self.actionCancel = QtWidgets.QAction(ProfileWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCancel.setIcon(icon2)
        self.actionCancel.setObjectName("actionCancel")
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.Edit)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionCancel)
        self.toolBar.addSeparator()

        self.retranslateUi(ProfileWindow)
        QtCore.QMetaObject.connectSlotsByName(ProfileWindow)

    def retranslateUi(self, ProfileWindow):
        _translate = QtCore.QCoreApplication.translate
        ProfileWindow.setWindowTitle(_translate("ProfileWindow", "Profile"))
        self.label_login.setText(_translate("ProfileWindow", "Login"))
        self.label_role.setText(_translate("ProfileWindow", "Role"))
        self.label_password.setText(_translate("ProfileWindow", "Password"))
        self.lbl_name2.setText(_translate("ProfileWindow", "First name"))
        self.lbl_name1.setText(_translate("ProfileWindow", "Last name"))
        self.lbl_name3.setText(_translate("ProfileWindow", "Patronymic"))
        self.label_warning.setText(_translate("ProfileWindow", "Missing bank detal information"))
        self.btn_add_provider.setText(_translate("ProfileWindow", "Add"))
        self.label_warning_2.setText(_translate("ProfileWindow", "Missing company name"))
        self.btn_administration.setText(_translate("ProfileWindow", "Administration"))
        self.btn_history.setText(_translate("ProfileWindow", "History"))
        self.btn_products.setText(_translate("ProfileWindow", "Store"))
        self.toolBar.setWindowTitle(_translate("ProfileWindow", "toolBar"))
        self.Edit.setText(_translate("ProfileWindow", "Edit"))
        self.Edit.setToolTip(_translate("ProfileWindow", "<html><head/><body><p>Edit</p></body></html>"))
        self.actionSave.setText(_translate("ProfileWindow", "Save"))
        self.actionSave.setToolTip(_translate("ProfileWindow", "Save"))
        self.actionCancel.setText(_translate("ProfileWindow", "Cancel"))
        self.actionCancel.setToolTip(_translate("ProfileWindow", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ProfileWindow = QtWidgets.QMainWindow()
    ui = Ui_ProfileWindow()
    ui.setupUi(ProfileWindow)
    ProfileWindow.show()
    sys.exit(app.exec_())
