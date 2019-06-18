from calculadorafinanceira.view.graficos import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow

class CalculadoraFinanciamentoGraficosView(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

    def renderizarGraficos(self, resultadoCalculo):
        self.ui.continueUiSetup(resultadoCalculo)