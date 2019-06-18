from PyQt5.QtWidgets import QApplication, QMainWindow
from calculadorafinanceira.view.CalculadoraFinanciamentoView import Ui_MainWindow

class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    w = AppWindow()
    w.setWindowTitle("Calculadora de Financiamento")
    w.show()
    sys.exit(app.exec_())