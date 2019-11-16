from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5.QtCore import Qt
from PyQt5 import uic

import sqlite3


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.setWindowTitle('Сорты Кофе')

        self.db = sqlite3.connect('coffee.sqlite')
        self.db_cursor = self.db.cursor()

        self.update_table()

    def get_coffee_frying(self, frying_id):
        return self.db_cursor.execute('SELECT name FROM frying_degrees WHERE id=?', [frying_id]).fetchall()[0][0]

    def get_coffee_frying_id(self, frying):
        return self.db_cursor.execute('SELECT id FROM frying_degrees WHERE name=?', [frying]).fetchall()[0][0]

    def get_coffee_type(self, coffee_type_id):
        return self.db_cursor.execute('SELECT name FROM types WHERE id=?', [coffee_type_id]).fetchall()[0][0]

    def get_coffee_type_id(self, coffee_type):
        return self.db_cursor.execute('SELECT id FROM types WHERE name=?', [coffee_type]).fetchall()[0][0]

    def get_coffees(self):
        return self.db_cursor.execute('SELECT * FROM sorts').fetchall()

    def update_table(self):
        self.tableWidget.setRowCount(0)

        for row, coffee in enumerate(self.get_coffees()):
            self.tableWidget.setRowCount(row + 1)
            for col, item in enumerate(coffee):
                if col == 2:
                    table_item = QTableWidgetItem(self.get_coffee_frying(item))
                elif col == 3:
                    table_item = QTableWidgetItem(self.get_coffee_type(item))
                else:
                    table_item = QTableWidgetItem(str(item))
                table_item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.tableWidget.setItem(row, col, table_item)
        self.tableWidget.resizeColumnsToContents()


def main():
    app = QApplication([])
    window = Window()
    window.show()
    exit(app.exec())


if __name__ == '__main__':
    main()