# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addEditCoffeeForm.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(283, 338)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.name_input = QtWidgets.QLineEdit(Dialog)
        self.name_input.setGeometry(QtCore.QRect(150, 20, 113, 20))
        self.name_input.setObjectName("name_input")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.frying_input = QtWidgets.QComboBox(Dialog)
        self.frying_input.setGeometry(QtCore.QRect(150, 60, 111, 22))
        self.frying_input.setObjectName("frying_input")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 100, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.coffee_type_input = QtWidgets.QComboBox(Dialog)
        self.coffee_type_input.setGeometry(QtCore.QRect(150, 100, 111, 22))
        self.coffee_type_input.setObjectName("coffee_type_input")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 140, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.description_input = QtWidgets.QLineEdit(Dialog)
        self.description_input.setGeometry(QtCore.QRect(150, 140, 113, 20))
        self.description_input.setObjectName("description_input")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 180, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.cost_input = QtWidgets.QSpinBox(Dialog)
        self.cost_input.setGeometry(QtCore.QRect(150, 180, 111, 22))
        self.cost_input.setObjectName("cost_input")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(20, 220, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.volume_input = QtWidgets.QSpinBox(Dialog)
        self.volume_input.setGeometry(QtCore.QRect(150, 220, 111, 22))
        self.volume_input.setObjectName("volume_input")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(90, 270, 111, 41))
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")

        Ui_Dialog.retranslateUi(Dialog, Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Название сорта:"))
        self.label_2.setText(_translate("Dialog", "Степень обжарки:"))
        self.label_3.setText(_translate("Dialog", "Вид кофе:"))
        self.label_4.setText(_translate("Dialog", "Описание вкуса:"))
        self.label_5.setText(_translate("Dialog", "Цена:"))
        self.label_6.setText(_translate("Dialog", "Объём в гр.:"))
