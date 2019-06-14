# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Downloads/prototipoCERTISSIMO.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QVBoxLayout, QAbstractItemView
from calculadorafinanceira.delegate.CalculadoraFinanciamentoDelegator import CalculadoraFinanciamentoDelegator
from calculadorafinanceira.model.SistemaFinanciamento import SistemaFinanciamento
from calculadorafinanceira.model.CalculadoraFinanciamentoTableModel import CalculadoraFinanciamentoTableModel

class Ui_MainWindow(object):

    estiloLineEditInvalido = "border-style: solid; border-width: 2px 2px 2px 2px; border-color: red;"
    cabecalhosTabelaResultado = ["Parcela", "Valor da Prestação", "Amortização", "Juros", "Saldo Devedor"]

    def __init__(self):
        self.calculadoraFinanciamentoDelegator = CalculadoraFinanciamentoDelegator(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBoxInput = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxInput.setTitle("")
        self.groupBoxInput.setObjectName("groupBoxInput")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBoxInput)
        self.gridLayout.setObjectName("gridLayout")
        self.labelValorDoBem = QtWidgets.QLabel(self.groupBoxInput)
        self.labelValorDoBem.setAlignment(QtCore.Qt.AlignCenter)
        self.labelValorDoBem.setObjectName("labelValorDoBem")
        self.gridLayout.addWidget(self.labelValorDoBem, 0, 0, 1, 1)
        self.labelTaxaDeJuros = QtWidgets.QLabel(self.groupBoxInput)
        self.labelTaxaDeJuros.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTaxaDeJuros.setObjectName("labelTaxaDeJuros")
        self.gridLayout.addWidget(self.labelTaxaDeJuros, 0, 1, 1, 1)
        self.labelNumeroDeParcelas = QtWidgets.QLabel(self.groupBoxInput)
        self.labelNumeroDeParcelas.setAlignment(QtCore.Qt.AlignCenter)
        self.labelNumeroDeParcelas.setObjectName("labelNumeroDeParcelas")
        self.gridLayout.addWidget(self.labelNumeroDeParcelas, 0, 2, 1, 1)
        self.labelSistemaDeFinanciamento = QtWidgets.QLabel(self.groupBoxInput)
        self.labelSistemaDeFinanciamento.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSistemaDeFinanciamento.setObjectName("labelSistemaDeFinanciamento")
        self.gridLayout.addWidget(self.labelSistemaDeFinanciamento, 0, 3, 1, 2)
        self.pushButtonSimular = QtWidgets.QPushButton(self.groupBoxInput)
        self.pushButtonSimular.setObjectName("pushButtonSimular")
        self.gridLayout.addWidget(self.pushButtonSimular, 0, 5, 1, 1)
        self.lineEditValorDoBem = QtWidgets.QLineEdit(self.groupBoxInput)
        self.lineEditValorDoBem.setObjectName("lineEditValorDoBem")
        self.lineEditValorDoBem.setText("1.000,00")
        self.gridLayout.addWidget(self.lineEditValorDoBem, 1, 0, 1, 1)
        self.lineEditTaxaDeJuros = QtWidgets.QLineEdit(self.groupBoxInput)
        self.lineEditTaxaDeJuros.setObjectName("lineEditTaxaDeJuros")
        self.lineEditTaxaDeJuros.setText("1")
        self.gridLayout.addWidget(self.lineEditTaxaDeJuros, 1, 1, 1, 1)
        self.lineEditNumeroDeParcelas = QtWidgets.QLineEdit(self.groupBoxInput)
        self.lineEditNumeroDeParcelas.setObjectName("lineEditNumeroDeParcelas")
        self.lineEditNumeroDeParcelas.setText("12")
        self.gridLayout.addWidget(self.lineEditNumeroDeParcelas, 1, 2, 1, 1)
        self.checkBoxSac = QtWidgets.QCheckBox(self.groupBoxInput)
        self.checkBoxSac.setObjectName("checkBoxSac")
        self.gridLayout.addWidget(self.checkBoxSac, 1, 3, 1, 1)
        self.checkBoxPrice = QtWidgets.QCheckBox(self.groupBoxInput)
        self.checkBoxPrice.setObjectName("checkBoxPrice")
        self.gridLayout.addWidget(self.checkBoxPrice, 1, 4, 1, 1)
        self.pushButtonResetar = QtWidgets.QPushButton(self.groupBoxInput)
        self.pushButtonResetar.setObjectName("pushButtonResetar")
        self.gridLayout.addWidget(self.pushButtonResetar, 1, 5, 1, 1)
        self.verticalLayout.addWidget(self.groupBoxInput)
        self.groupBoxResultado = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxResultado.setTitle("")
        self.groupBoxResultado.setObjectName("groupBoxResultado")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBoxResultado)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableViewResultado = QtWidgets.QTableView(self.groupBoxResultado)
        self.tableViewResultado.setObjectName("tableViewResultado")
        self.verticalLayout_2.addWidget(self.tableViewResultado)
        self.verticalLayout.addWidget(self.groupBoxResultado)
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

        self.continueUiSetup()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelValorDoBem.setText(_translate("MainWindow", "Valor do bem"))
        self.labelTaxaDeJuros.setText(_translate("MainWindow", "Taxa de Juros"))
        self.labelNumeroDeParcelas.setText(_translate("MainWindow", "Numero de Parcelas"))
        self.labelSistemaDeFinanciamento.setText(_translate("MainWindow", "Sistema de Financiamento"))
        self.pushButtonSimular.setText(_translate("MainWindow", "Simular"))
        self.checkBoxSac.setText(_translate("MainWindow", "SAC"))
        self.checkBoxPrice.setText(_translate("MainWindow", "PRICE"))
        self.pushButtonResetar.setText(_translate("MainWindow", "Resetar"))

    def continueUiSetup(self):
        self.pushButtonSimular.clicked.connect(self.onClickPushButtonSimular)
        self.pushButtonResetar.clicked.connect(self.onClickPushButtonResetar)

    def onClickPushButtonSimular(self):
        sistemasFinanciamento = []
        if self.checkBoxSac.isChecked():
            sistemasFinanciamento.append(SistemaFinanciamento.SAC)
        if self.checkBoxPrice.isChecked():
            sistemasFinanciamento.append(SistemaFinanciamento.PRICE)

        resultadoCalculo = self.calculadoraFinanciamentoDelegator.calcula_financiamento(
            self.lineEditValorDoBem.text(), 
            self.lineEditTaxaDeJuros.text(), 
            self.lineEditNumeroDeParcelas.text(), 
            sistemasFinanciamento
            )

        self.renderizarTabela(resultadoCalculo)

    def onClickPushButtonResetar(self):
        self.lineEditValorDoBem.clear()
        self.lineEditTaxaDeJuros.clear()
        self.lineEditNumeroDeParcelas.clear()
        self.valoresValidosInput()

    def valorInvalidoLineEditValorDoBem(self):
        self.lineEditValorDoBem.setStyleSheet(
            "#" + self.lineEditValorDoBem.objectName() + "{" + 
            self.estiloLineEditInvalido + 
            "}")

    def valorInvalidoLineEditTaxaDeJuros(self):
        self.lineEditTaxaDeJuros.setStyleSheet(
            "#" + self.lineEditTaxaDeJuros.objectName() + "{" + 
            self.estiloLineEditInvalido + 
            "}")

    def valorInvalidoLineEditNumeroDeParcelas(self):
        self.lineEditNumeroDeParcelas.setStyleSheet(
            "#" + self.lineEditNumeroDeParcelas.objectName() + "{" + 
            self.estiloLineEditInvalido + 
            "}")

    def sistemaDeFinanciamentoNaoEscolhido(self):
        self.checkBoxSac.setStyleSheet(
            "#" + self.checkBoxSac.objectName() + "{" +
            self.estiloLineEditInvalido +
            "}")
        
        self.checkBoxPrice.setStyleSheet(
            "#" + self.checkBoxPrice.objectName() + "{" +
            self.estiloLineEditInvalido +
            "}")

    # Remove a borda vermelha dos campos de input
    def valoresValidosInput(self):
        self.lineEditValorDoBem.setStyleSheet("")
        self.lineEditTaxaDeJuros.setStyleSheet("")
        self.lineEditNumeroDeParcelas.setStyleSheet("")
        self.checkBoxSac.setStyleSheet("")
        self.checkBoxPrice.setStyleSheet("")

    def renderizarTabela(self, resultadoCalculo):
        if (resultadoCalculo.getResultadoSac() is None):
            self.renderizarSistemaCalculoUnico(resultadoCalculo.getResultadoPrice())
        elif (resultadoCalculo.getResultadoPrice() is None):
            self.renderizarSistemaCalculoUnico(resultadoCalculo.getResultadoSac())
        else:
            self.renderizarSistemaCalculoMultiplo(resultadoCalculo)

    def renderizarSistemaCalculoUnico(self, linhas):
        self.tableModel = CalculadoraFinanciamentoTableModel(linhas, self.cabecalhosTabelaResultado)
        self.tableViewResultado.setModel(self.tableModel)
        self.tableViewResultado.resizeColumnsToContents()
        self.tableViewResultado.setSpan(len(linhas) - 1, 1, 1, 4)

    def renderizarSistemaCalculoMultiplo(self, resultadoCalculo):
        linhas = [x + y for x, y in zip(resultadoCalculo.getResultadoSac(), resultadoCalculo.getResultadoPrice())]
        self.tableModel = CalculadoraFinanciamentoTableModel(linhas, self.cabecalhosTabelaResultado * 2)
        self.tableViewResultado.setModel(self.tableModel)
        self.tableViewResultado.resizeColumnsToContents()
        self.tableViewResultado.setSpan(len(linhas) - 1, 1, 1, 4)
        self.tableViewResultado.setSpan(len(linhas) - 1, 6, 1, 4)