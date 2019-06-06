from calculadorafinanceira.model.SistemaFinanciamento import SistemaFinanciamento

class CalculadoraFinanciamento:
    
    def calcula_financiamento(self, valor_bem, taxa_juros, num_parcelas, sistema_financiamento):
        if (sistema_financiamento is SistemaFinanciamento.PRICE):
            self.calcula_financiamento_price(valor_bem, taxa_juros, num_parcelas, sistema_financiamento)
        elif (sistema_financiamento is SistemaFinanciamento.SAC):
            self.calcula_financiamento_sac(valor_bem, taxa_juros, num_parcelas, sistema_financiamento)
        
    def calcula_financiamento_price(self, valor_bem, taxa_juros, num_parcelas, sistema_financiamento):
        pass

    def calcula_financiamento_sac(self, valor_bem, taxa_juros, num_parcelas, sistema_financiamento):
        pass