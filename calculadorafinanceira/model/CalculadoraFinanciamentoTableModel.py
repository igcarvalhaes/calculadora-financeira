from PyQt5.QtCore import QAbstractTableModel, QVariant, Qt

class CalculadoraFinanciamentoTableModel(QAbstractTableModel):
    
    def __init__(self, linhas, cabecalhos, parent=None, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self.linhas = linhas
        self.cabecalhos = cabecalhos
    
    def rowCount(self, parent):
        return len(self.linhas)
    
    def columnCount(self, parent):
        return len(self.linhas[0])

    def data(self, index, role):
        if not index.isValid(): 
            return QVariant() 
        elif role != Qt.DisplayRole: 
            return QVariant()
        return QVariant(self.linhas[index.row()][index.column()])

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return QVariant(self.cabecalhos[col])
        return QVariant()