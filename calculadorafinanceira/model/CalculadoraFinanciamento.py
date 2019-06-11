from calculadorafinanceira.model.SistemaFinanciamento import SistemaFinanciamento
import locale

class CalculadoraFinanciamento:
    
    def calcula_financiamento(self, valor_bem, taxa_juros, num_parcelas, sistema_financiamento):
        if (sistema_financiamento is SistemaFinanciamento.PRICE):
            self.calcula_financiamento_price(valor_bem, taxa_juros, num_parcelas, sistema_financiamento)
        elif (sistema_financiamento is SistemaFinanciamento.SAC):
            self.calcula_financiamento_sac(valor_bem, taxa_juros, num_parcelas, sistema_financiamento)
        
    def calcula_financiamento_price(self, valor_bem, taxa_juros, num_parcelas, sistema_financiamento):
        linhas = []
        valor_parcelas = valor_bem*((((1+taxa_juros/100)**num_parcelas)*taxa_juros/100)/(((1+taxa_juros/100)**num_parcelas)-1))
        juros = valor_bem * (taxa_juros / 100)
        amortizacao = valor_parcelas - juros
        linhas.append([0,0,0,0, valor_bem])
        for i in range(1, num_parcelas+1):
            juros = valor_bem * (taxa_juros / 100)
            valor_bem = (valor_bem * (1 + (taxa_juros / 100))**(1-valor_parcelas)) 
            amortizacao = valor_parcelas - juros
            linhas.append([i, valor_parcelas, amortizacao, juros, valor_bem])
        return linhas

    def calcula_financiamento_sac(self, valor_bem, taxa_juros, num_parcelas, sistema_financiamento):
        linhas = []
        amortizacao = valor_bem / num_parcelas
        linhas.append([0, 0, 0, 0, valor_bem])
        for i in range(1, num_parcelas + 1):
            juros = valor_bem * (taxa_juros / 100)
            prestacao = juros + amortizacao
            valor_bem -= amortizacao
            linhas.append([i, prestacao, amortizacao, juros, valor_bem])
        return linhas
