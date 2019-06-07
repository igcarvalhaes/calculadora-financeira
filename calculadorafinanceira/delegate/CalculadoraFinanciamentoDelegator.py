from calculadorafinanceira.model.CalculadoraFinanciamento import CalculadoraFinanciamento
from calculadorafinanceira.model.SistemaFinanciamento import SistemaFinanciamento
from calculadorafinanceira.model.FormatoInputCalculadoraFinanciamento import FormatoInputCalculadoraFinanciamento
from calculadorafinanceira.view.CalculadoraFinanciamentoView import *

import re

class CalculadoraFinanciamentoDelegator:
    
    def __init__(self, Ui_MainWindow):
        self.calculadoraFinanciamentoView = Ui_MainWindow
        self.calculadoraFinanciamento = CalculadoraFinanciamento()

    def calcula_financiamento(self, valor_bem, taxa_juros, num_parcelas, sistema_financiamento):
        self.calculadoraFinanciamentoView.valoresValidosInput()        

        if not re.match(FormatoInputCalculadoraFinanciamento.FORMATO_VALOR_DO_BEM.value, valor_bem):
            self.calculadoraFinanciamentoView.valorInvalidoLineEditValorDoBem()
        elif not re.match(FormatoInputCalculadoraFinanciamento.FORMATO_TAXA_DE_JUROS.value, taxa_juros):
            self.calculadoraFinanciamentoView.valorInvalidoLineEditTaxaDeJuros()
        elif not re.match(FormatoInputCalculadoraFinanciamento.FORMATO_NUMERO_DE_PARCELAS.value, num_parcelas):
            self.calculadoraFinanciamentoView.valorInvalidoLineEditNumeroDeParcelas()
        else:
            return self.calculadoraFinanciamento.calcula_financiamento(valor_bem=valor_bem, taxa_juros=taxa_juros, num_parcelas=num_parcelas, sistema_financiamento=sistema_financiamento)