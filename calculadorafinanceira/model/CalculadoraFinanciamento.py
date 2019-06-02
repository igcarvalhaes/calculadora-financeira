from calculadorafinanceira.model.SistemaFinanciamento import SistemaFinanciamento

class CalculadoraFinanciamentoSacPrice:
    
    def calcula_financiamento(self, valor_bem, taxa_juros, num_parcelas, sistema_financiamento):
        if (sistema_financiamento is SistemaFinanciamento.PRICE):
            pass
        elif (sistema_financiamento is SistemaFinanciamento.SAC):
            pass
        
    def calcula_financiamento_price(self, valor_bem, taxa_juros, num_parcelas, sistema_financiamento):
        pass

    def calcula_financiamento_sac(self, valor_bem, taxa_juros, num_parcelas, sistema_financiamento):
        pass