# python -m PyQt5.uic.pyuic -x Administration.ui -o Administration.py
from PyQt5 import QtWidgets
from Forms.LoginForm import LoginWindow
from Service.DBHelper import DBHelper


def main():
    my_db = DBHelper()
    my_db.cursor.execute('SET GLOBAL event_scheduler=ON')
    my_db.cursor.fetchone()
    my_db.connect.commit()
    app = QtWidgets.QApplication([])  # Новый экземпляр QApplication
    window = LoginWindow(my_db)  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':
    main()
