import locale
from PyQt5.QtCore import QAbstractTableModel, QVariant, Qt
from numbers import Number

class CalculadoraFinanciamentoTableModel(QAbstractTableModel):
    
    def __init__(self, linhas, cabecalhos, parent=None, *args):
        QAbstractTableModel.__init__(self, parent, *args)

        self.linhas = linhas
        self.cabecalhos = cabecalhos
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    
    def rowCount(self, parent):
        return len(self.linhas)
    
    def columnCount(self, parent):
        return len(self.linhas[0])

    def data(self, index, role):
        if not index.isValid(): 
            return QVariant() 
        elif role != Qt.DisplayRole: 
            return QVariant()
            
        # Formata para valor monetário se nao for a primeira coluna
        dado = self.linhas[index.row()][index.column()]
        if index.column() == 0:
            return (QVariant(dado))
        elif type(dado) is not str:
            return QVariant(locale.currency(dado, grouping=True))
        
    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return QVariant(self.cabecalhos[col])
        return QVariant()