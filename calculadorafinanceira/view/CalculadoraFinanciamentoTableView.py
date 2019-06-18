from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableView

class CalculadoraFinanciamentoTableView(QTableView):

    nomeWidget = None
    instances = []

    def __init__(self, parent):
        super().__init__(parent=parent)
        self.instances.append(self)

    def wheelEvent(self, QWheelEvent):
        if self.nomeWidget is None:
            self.nomeWidget = self.objectName()
            for instance in self.instances:
                super(QTableView, instance).wheelEvent(QWheelEvent)
            self.nomeWidget = None

    def deleteLater(self):
        self.instances.remove(self)
        return super().deleteLater()