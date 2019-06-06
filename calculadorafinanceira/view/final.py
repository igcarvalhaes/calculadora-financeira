# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Desktop/prototipo.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from calculadorafinanceira.delegate.CalculadoraFinanciamentoDelegator import CalculadoraFinanciamentoDelegator
from calculadorafinanceira.model.SistemaFinanciamento import SistemaFinanciamento

class Ui_MainWindow(object):

    def __init__(self):
        self.calculadoraFinanciamentoDelegator = CalculadoraFinanciamentoDelegator(self)
        self.estiloInputInvalido = "border-style: solid; border-width: 2px 2px 2px 2px; border-color: red;"

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Calculadora de Financiamento")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBoxInput = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxInput.setGeometry(QtCore.QRect(0, 0, 800, 100))
        self.groupBoxInput.setTitle("")
        self.groupBoxInput.setObjectName("groupBoxInput")
        self.pushButtonSimular = QtWidgets.QPushButton(self.groupBoxInput)
        self.pushButtonSimular.setGeometry(QtCore.QRect(700, 10, 87, 29))
        self.pushButtonSimular.setObjectName("pushButtonSimular")
        self.pushButtonSimular.clicked.connect(self.onClickPushButtonSimular)
        self.pushButtonResetar = QtWidgets.QPushButton(self.groupBoxInput)
        self.pushButtonResetar.setGeometry(QtCore.QRect(700, 60, 87, 29))
        self.pushButtonResetar.setObjectName("pushButtonResetar")
        self.pushButtonResetar.clicked.connect(self.onClickPushButtonResetar)
        self.labelValorDoBem = QtWidgets.QLabel(self.groupBoxInput)
        self.labelValorDoBem.setGeometry(QtCore.QRect(10, 30, 150, 20))
        self.labelValorDoBem.setAlignment(QtCore.Qt.AlignCenter)
        self.labelValorDoBem.setObjectName("labelValorDoBem")
        self.lineEditValorDoBem = QtWidgets.QLineEdit(self.groupBoxInput)
        self.lineEditValorDoBem.setGeometry(QtCore.QRect(10, 60, 150, 25))
        self.lineEditValorDoBem.setObjectName("lineEditValorDoBem")
        self.labelTaxaDeJuros = QtWidgets.QLabel(self.groupBoxInput)
        self.labelTaxaDeJuros.setGeometry(QtCore.QRect(170, 30, 150, 20))
        self.labelTaxaDeJuros.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTaxaDeJuros.setObjectName("labelTaxaDeJuros")
        self.labelNumeroDeParcelas = QtWidgets.QLabel(self.groupBoxInput)
        self.labelNumeroDeParcelas.setGeometry(QtCore.QRect(330, 30, 150, 20))
        self.labelNumeroDeParcelas.setAlignment(QtCore.Qt.AlignCenter)
        self.labelNumeroDeParcelas.setObjectName("labelNumeroDeParcelas")
        self.labelSistemaDeFinanciamento = QtWidgets.QLabel(self.groupBoxInput)
        self.labelSistemaDeFinanciamento.setGeometry(QtCore.QRect(490, 30, 150, 20))
        self.labelSistemaDeFinanciamento.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSistemaDeFinanciamento.setObjectName("labelSistemaDeFinanciamento")
        self.lineEditTaxaDeJuros = QtWidgets.QLineEdit(self.groupBoxInput)
        self.lineEditTaxaDeJuros.setGeometry(QtCore.QRect(170, 60, 150, 25))
        self.lineEditTaxaDeJuros.setObjectName("lineEditTaxaDeJuros")
        self.lineEditNumeroDeParcelas = QtWidgets.QLineEdit(self.groupBoxInput)
        self.lineEditNumeroDeParcelas.setGeometry(QtCore.QRect(330, 60, 150, 25))
        self.lineEditNumeroDeParcelas.setObjectName("lineEditNumeroDeParcelas")
        self.radioButtonSac = QtWidgets.QRadioButton(self.groupBoxInput)
        self.radioButtonSac.setGeometry(QtCore.QRect(490, 60, 75, 25))
        self.radioButtonSac.setObjectName("radioButtonSac")
        self.radioButtonSac.setChecked(True)
        self.radioButtonPrice = QtWidgets.QRadioButton(self.groupBoxInput)
        self.radioButtonPrice.setGeometry(QtCore.QRect(565, 60, 75, 25))
        self.radioButtonPrice.setObjectName("radioButtonPrice")
        self.groupBoxResultado = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxResultado.setGeometry(QtCore.QRect(0, 100, 800, 500))
        self.groupBoxResultado.setTitle("")
        self.groupBoxResultado.setObjectName("groupBoxResultado")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButtonSimular.setText(_translate("MainWindow", "Simular"))
        self.pushButtonResetar.setText(_translate("MainWindow", "Resetar"))
        self.labelValorDoBem.setText(_translate("MainWindow", "Valor do bem"))
        self.labelTaxaDeJuros.setText(_translate("MainWindow", "Taxa de Juros"))
        self.labelNumeroDeParcelas.setText(_translate("MainWindow", "Numero de Parcelas"))
        self.labelSistemaDeFinanciamento.setText(_translate("MainWindow", "Sistema de Financiamento"))
        self.radioButtonSac.setText(_translate("MainWindow", "SAC"))
        self.radioButtonPrice.setText(_translate("MainWindow", "PRICE"))

    def onClickPushButtonSimular(self):
        return self.calculadoraFinanciamentoDelegator.calcula_financiamento(
            self.lineEditValorDoBem.text(), 
            self.lineEditTaxaDeJuros.text(), 
            self.lineEditNumeroDeParcelas.text(), 
            SistemaFinanciamento.PRICE if self.radioButtonPrice.isChecked() else SistemaFinanciamento.SAC
            )

    def onClickPushButtonResetar(self):
        self.lineEditValorDoBem.clear()
        self.lineEditTaxaDeJuros.clear()
        self.lineEditNumeroDeParcelas.clear()
        # TODO: resetar a tabela

    def valorInvalidoLineEditValorDoBem(self):
        self.lineEditValorDoBem.setStyleSheet(
            "#" + self.lineEditValorDoBem.objectName() + "{" + 
            self.estiloInputInvalido + 
            "}")

    def valorInvalidoLineEditTaxaDeJuros(self):
        self.lineEditTaxaDeJuros.setStyleSheet(
            "#" + self.lineEditTaxaDeJuros.objectName() + "{" + 
            self.estiloInputInvalido + 
            "}")

    def valorInvalidoLineEditNumeroDeParcelas(self):
        self.lineEditNumeroDeParcelas.setStyleSheet(
            "#" + self.lineEditNumeroDeParcelas.objectName() + "{" + 
            self.estiloInputInvalido + 
            "}")

    def valoresValidosInput(self):
        self.lineEditValorDoBem.setStyleSheet("")
        self.lineEditTaxaDeJuros.setStyleSheet("")
        self.lineEditNumeroDeParcelas.setStyleSheet("")