from calculadorafinanceira.model.CalculadoraFinanciamento import CalculadoraFinanciamento
from calculadorafinanceira.model.SistemaFinanciamento import SistemaFinanciamento
from calculadorafinanceira.model.FormatoInputCalculadoraFinanciamento import FormatoInputCalculadoraFinanciamento
from calculadorafinanceira.view.CalculadoraFinanciamentoView import *

import re

class CalculadoraFinanciamentoDelegator:
    
    def __init__(self, Ui_MainWindow):
        self.calculadoraFinanciamentoView = Ui_MainWindow
        self.calculadoraFinanciamento = CalculadoraFinanciamento()

    def calcula_financiamento(self, valor_bem, taxa_juros, num_parcelas, sistemasFinanciamento):
        self.calculadoraFinanciamentoView.valoresValidosInput()        

        if not re.match(FormatoInputCalculadoraFinanciamento.FORMATO_VALOR_DO_BEM.value, valor_bem):
            self.calculadoraFinanciamentoView.valorInvalidoLineEditValorDoBem()
        elif not re.match(FormatoInputCalculadoraFinanciamento.FORMATO_TAXA_DE_JUROS.value, taxa_juros):
            self.calculadoraFinanciamentoView.valorInvalidoLineEditTaxaDeJuros()
        elif not re.match(FormatoInputCalculadoraFinanciamento.FORMATO_NUMERO_DE_PARCELAS.value, num_parcelas):
            self.calculadoraFinanciamentoView.valorInvalidoLineEditNumeroDeParcelas()
        elif len(sistemasFinanciamento) == 0:
            self.calculadoraFinanciamentoView.sistemaDeFinanciamentoNaoEscolhido()
        else:
            resultadoCalculo = self.calculadoraFinanciamento.calcula_financiamento(
                float(valor_bem.replace(".", "").replace(",", ".")),
                int(taxa_juros),
                int(num_parcelas),
                sistemasFinanciamento
                )
            
            self.calculadoraFinanciamentoView.limparGroupBoxResultado()
            self.calculadoraFinanciamentoView.renderizarTabelaResultado(resultadoCalculo)
            self.calculadoraFinanciamentoView.renderizarGraficoResultado(resultadoCalculo)