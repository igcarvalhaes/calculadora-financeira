from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableView

class CalculadoraFinanciamentoTableView(QTableView):

    estaAtualizando = False
    instances = []

    def __init__(self, parent):
        super().__init__(parent=parent)
        self.instances.append(self)

    def wheelEvent(self, QWheelEvent):
        if not self.estaAtualizando:
            self.estaAtualizando = True
            for instance in self.instances:
                super(QTableView, instance).wheelEvent(QWheelEvent)
            self.estaAtualizando = False

    def deleteLater(self):
        self.instances.remove(self)
        return super().deleteLater()