from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QAction, QMessageBox, QDialog
from PyQt5.QtCore import Qt

from mainUI import Ui_MainWindow
from addEditCoffeeForm import Ui_Dialog

import sqlite3


class Window(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Сорты Кофе')

        self.db = sqlite3.connect('data\\coffee.sqlite')
        self.db_cursor = self.db.cursor()

        add_coffee_action = QAction('Добавить кофе', self)
        add_coffee_action.triggered.connect(self.add_coffee_dialog)
        self.menuBar.addAction(add_coffee_action)

        change_coffee_action = QAction('Изменить выбранный кофе', self)
        change_coffee_action.triggered.connect(self.change_coffee_dialog)
        self.menuBar.addAction(change_coffee_action)

        self.update_table()

    def get_coffee_frying(self, frying_id):
        return self.db_cursor.execute('SELECT name FROM frying_degrees WHERE id=?', [frying_id]).fetchall()[0][0]

    def get_coffee_fryings(self):
        from operator import itemgetter
        return map(itemgetter(0), self.db_cursor.execute('SELECT name FROM frying_degrees').fetchall())

    def get_coffee_frying_id(self, frying):
        return self.db_cursor.execute('SELECT id FROM frying_degrees WHERE name=?', [frying]).fetchall()[0][0]

    def get_coffee_type(self, coffee_type_id):
        return self.db_cursor.execute('SELECT name FROM types WHERE id=?', [coffee_type_id]).fetchall()[0][0]

    def get_coffee_types(self):
        from operator import itemgetter
        return map(itemgetter(0), self.db_cursor.execute('SELECT name FROM types').fetchall())

    def get_coffee_type_id(self, coffee_type):
        return self.db_cursor.execute('SELECT id FROM types WHERE name=?', [coffee_type]).fetchall()[0][0]

    def get_coffees(self):
        return self.db_cursor.execute('SELECT * FROM sorts').fetchall()

    def get_coffee(self, coffee_id):
        return self.db_cursor.execute('SELECT * FROM sorts WHERE id=?', [coffee_id]).fetchall()[0]

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

    def add_coffee_dialog(self):
        dialog = QDialog()
        Ui_Dialog.setupUi(dialog, dialog)

        dialog.setWindowTitle('Добавить кофе')

        dialog.frying_input.addItems(self.get_coffee_fryings())
        dialog.coffee_type_input.addItems(self.get_coffee_types())

        dialog.cost_input.setMaximum(100000)
        dialog.volume_input.setMaximum(100000)

        def button_clicked():
            if not dialog.name_input.text():
                QMessageBox().question(dialog, '', 'Нужно ввести название кофе!', QMessageBox.Ok)
            else:
                name = dialog.name_input.text()
                frying = self.get_coffee_frying_id(dialog.frying_input.currentText())
                coffee_type = self.get_coffee_type_id(dialog.coffee_type_input.currentText())
                description = dialog.description_input.text() or 'Отсутствует'
                cost = int(dialog.cost_input.text())
                volume = int(dialog.volume_input.text())

                self.db_cursor.execute('INSERT INTO sorts(name, frying_degree, type, taste, cost, volume)'
                                       ' VALUES(?, ?, ?, ?, ?, ?)',
                                       [name, frying, coffee_type, description, cost, volume])

                QMessageBox().question(self, '', 'Кофе успешно добавлен в базу!', QMessageBox.Ok)
                self.update_table()
                dialog.close()

        dialog.pushButton.setText('Добавить')
        dialog.pushButton.clicked.connect(button_clicked)

        dialog.exec()

    def change_coffee_dialog(self):
        if not self.tableWidget.selectionModel().hasSelection():
            QMessageBox().question(self, '', 'Сначала выделите кофе из таблицы', QMessageBox.Ok)
        else:
            dialog = QDialog()
            Ui_Dialog.setupUi(dialog, dialog)

            coffee = self.get_coffee(self.tableWidget.item(self.tableWidget.currentRow(), 0).text())

            dialog.name_input.setText(coffee[1])

            dialog.frying_input.addItems(self.get_coffee_fryings())
            dialog.frying_input.setCurrentIndex(coffee[2] - 1)

            dialog.coffee_type_input.addItems(self.get_coffee_types())
            dialog.coffee_type_input.setCurrentIndex(coffee[3] - 1)

            dialog.cost_input.setMaximum(100000)
            dialog.volume_input.setMaximum(100000)

            dialog.description_input.setText(coffee[4])

            dialog.cost_input.setValue(coffee[5])

            dialog.volume_input.setValue(coffee[6])

            def button_clicked():
                if not dialog.name_input.text():
                    QMessageBox().question(dialog, '', 'Нужно ввести название сорта!', QMessageBox.Ok)
                else:
                    name = dialog.name_input.text()
                    frying = self.get_coffee_frying_id(dialog.frying_input.currentText())
                    coffee_type = self.get_coffee_type_id(dialog.coffee_type_input.currentText())
                    description = dialog.description_input.text() or 'Отсутствует'
                    cost = int(dialog.cost_input.text())
                    volume = int(dialog.volume_input.text())

                    self.db_cursor.execute('UPDATE sorts SET name=? WHERE id=?', [name, coffee[0]])
                    self.db_cursor.execute('UPDATE sorts SET frying_degree=? WHERE id=?', [frying, coffee[0]])
                    self.db_cursor.execute('UPDATE sorts SET type=? WHERE id=?', [coffee_type, coffee[0]])
                    self.db_cursor.execute('UPDATE sorts SET taste=? WHERE id=?', [description, coffee[0]])
                    self.db_cursor.execute('UPDATE sorts SET cost=? WHERE id=?', [cost, coffee[0]])
                    self.db_cursor.execute('UPDATE sorts SET volume=? WHERE id=?', [volume, coffee[0]])

                    self.update_table()
                    dialog.close()

            dialog.pushButton.setText('Изменить')
            dialog.pushButton.clicked.connect(button_clicked)

            dialog.exec()

    def closeEvent(self, event):
        self.db.commit()
        self.db.close()


def main():
    app = QApplication([])
    app.setStyle('fusion')
    window = Window()
    window.show()
    exit(app.exec())


if __name__ == '__main__':
    main()