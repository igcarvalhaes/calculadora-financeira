class ResultadoCalculoFinanciamento:

    def __init__(self, resultadoSac, resultadoPrice):
        self.resultadoSac = resultadoSac
        self.resultadoPrice = resultadoPrice

    def getResultadoSac(self):
        return self.resultadoSac
    
    def getResultadoPrice(self):
        return self.resultadoPrice