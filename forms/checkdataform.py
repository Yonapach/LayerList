# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'checkdataform.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_checkDataForm(object):
    def setupUi(self, checkDataForm):
        checkDataForm.setObjectName("checkDataForm")
        checkDataForm.setEnabled(True)
        checkDataForm.resize(497, 236)
        self.gridLayout = QtWidgets.QGridLayout(checkDataForm)
        self.gridLayout.setObjectName("gridLayout")
        self.label_7 = QtWidgets.QLabel(checkDataForm)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 2)
        self.label_5 = QtWidgets.QLabel(checkDataForm)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.ui_tegListLbl = QtWidgets.QLabel(checkDataForm)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.ui_tegListLbl.setFont(font)
        self.ui_tegListLbl.setObjectName("ui_tegListLbl")
        self.gridLayout.addWidget(self.ui_tegListLbl, 8, 2, 1, 1)
        self.ui_okBtn = QtWidgets.QPushButton(checkDataForm)
        self.ui_okBtn.setObjectName("ui_okBtn")
        self.gridLayout.addWidget(self.ui_okBtn, 9, 2, 1, 1)
        self.ui_tzVerLbl = QtWidgets.QLabel(checkDataForm)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.ui_tzVerLbl.setFont(font)
        self.ui_tzVerLbl.setObjectName("ui_tzVerLbl")
        self.gridLayout.addWidget(self.ui_tzVerLbl, 1, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(checkDataForm)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.ui_techFamilyLbl = QtWidgets.QLabel(checkDataForm)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.ui_techFamilyLbl.setFont(font)
        self.ui_techFamilyLbl.setObjectName("ui_techFamilyLbl")
        self.gridLayout.addWidget(self.ui_techFamilyLbl, 5, 2, 1, 1)
        self.label = QtWidgets.QLabel(checkDataForm)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(checkDataForm)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.ui_projNameLbl = QtWidgets.QLabel(checkDataForm)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.ui_projNameLbl.setFont(font)
        self.ui_projNameLbl.setObjectName("ui_projNameLbl")
        self.gridLayout.addWidget(self.ui_projNameLbl, 0, 2, 1, 1)
        self.ui_projTypeLbl = QtWidgets.QLabel(checkDataForm)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.ui_projTypeLbl.setFont(font)
        self.ui_projTypeLbl.setObjectName("ui_projTypeLbl")
        self.gridLayout.addWidget(self.ui_projTypeLbl, 0, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(checkDataForm)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 7, 0, 1, 1)
        self.ui_regTypeLbl = QtWidgets.QLabel(checkDataForm)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.ui_regTypeLbl.setFont(font)
        self.ui_regTypeLbl.setObjectName("ui_regTypeLbl")
        self.gridLayout.addWidget(self.ui_regTypeLbl, 2, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(checkDataForm)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.ui_maskTypeLbl = QtWidgets.QLabel(checkDataForm)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.ui_maskTypeLbl.setFont(font)
        self.ui_maskTypeLbl.setObjectName("ui_maskTypeLbl")
        self.gridLayout.addWidget(self.ui_maskTypeLbl, 4, 2, 1, 1)
        self.ui_baseRouteLbl = QtWidgets.QLabel(checkDataForm)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.ui_baseRouteLbl.setFont(font)
        self.ui_baseRouteLbl.setObjectName("ui_baseRouteLbl")
        self.gridLayout.addWidget(self.ui_baseRouteLbl, 6, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(checkDataForm)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(checkDataForm)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 8, 0, 1, 2)
        self.ui_optionLbl = QtWidgets.QLabel(checkDataForm)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.ui_optionLbl.setFont(font)
        self.ui_optionLbl.setObjectName("ui_optionLbl")
        self.gridLayout.addWidget(self.ui_optionLbl, 7, 2, 1, 1)
        self.ui_maskSetNumLbl = QtWidgets.QLabel(checkDataForm)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.ui_maskSetNumLbl.setFont(font)
        self.ui_maskSetNumLbl.setObjectName("ui_maskSetNumLbl")
        self.gridLayout.addWidget(self.ui_maskSetNumLbl, 3, 2, 1, 1)
        self.ui_cancelBtn = QtWidgets.QPushButton(checkDataForm)
        self.ui_cancelBtn.setObjectName("ui_cancelBtn")
        self.gridLayout.addWidget(self.ui_cancelBtn, 9, 1, 1, 1)
        self.label.setBuddy(self.label)

        self.retranslateUi(checkDataForm)
        QtCore.QMetaObject.connectSlotsByName(checkDataForm)

    def retranslateUi(self, checkDataForm):
        _translate = QtCore.QCoreApplication.translate
        checkDataForm.setWindowTitle(_translate("checkDataForm", "Введённые данные"))
        self.label_7.setText(_translate("checkDataForm", "Базовые маршруты:"))
        self.label_5.setText(_translate("checkDataForm", "Тип шаблона:"))
        self.ui_tegListLbl.setText(_translate("checkDataForm", "TextLabel"))
        self.ui_okBtn.setText(_translate("checkDataForm", "Всё правильно"))
        self.ui_tzVerLbl.setText(_translate("checkDataForm", "TextLabel"))
        self.label_3.setText(_translate("checkDataForm", "Реестр"))
        self.ui_techFamilyLbl.setText(_translate("checkDataForm", "TextLabel"))
        self.label.setText(_translate("checkDataForm", "Название запуска:"))
        self.label_6.setText(_translate("checkDataForm", "Семейство технологий:"))
        self.ui_projNameLbl.setText(_translate("checkDataForm", "TextLabel"))
        self.ui_projTypeLbl.setText(_translate("checkDataForm", "TextLabel"))
        self.label_8.setText(_translate("checkDataForm", "Опции:"))
        self.ui_regTypeLbl.setText(_translate("checkDataForm", "TextLabel"))
        self.label_2.setText(_translate("checkDataForm", "Версия ТЗ:"))
        self.ui_maskTypeLbl.setText(_translate("checkDataForm", "TextLabel"))
        self.ui_baseRouteLbl.setText(_translate("checkDataForm", "TextLabel"))
        self.label_4.setText(_translate("checkDataForm", "Номер комплекта ФШ:"))
        self.label_9.setText(_translate("checkDataForm", "Тестовые сборки:"))
        self.ui_optionLbl.setText(_translate("checkDataForm", "TextLabel"))
        self.ui_maskSetNumLbl.setText(_translate("checkDataForm", "TextLabel"))
        self.ui_cancelBtn.setText(_translate("checkDataForm", "Всё неправильно"))
