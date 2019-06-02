import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem

class CalculadoraFinanciamentoView(QWidget):
    
    def __init__(self):
        super().__init__()
        self.title = "Calculadora de financiamento pelo sistema SAC/PRICE"
        self.left = 0
        self.top = 0
        self.height = 800
        self.width = 600

    def renderiza_tabela(self, linhas):
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(len(linhas))
        self.tableWidget.setColumnCount(5)
