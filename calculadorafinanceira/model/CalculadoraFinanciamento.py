from calculadorafinanceira.model.SistemaFinanciamento import SistemaFinanciamento
from calculadorafinanceira.model.ResultadoCalculoFinanciamento import ResultadoCalculoFinanciamento
import locale

class CalculadoraFinanciamento:
    
    def calcula_financiamento(self, valor_bem, taxa_juros, num_parcelas, sistemasDeFinanciamento):
        resultadoPrice = self.calcula_financiamento_price(
            valor_bem, 
            taxa_juros, 
            num_parcelas) if SistemaFinanciamento.PRICE in sistemasDeFinanciamento else None
        
        resultadoSac = self.calcula_financiamento_sac(
            valor_bem, 
            taxa_juros, 
            num_parcelas) if SistemaFinanciamento.SAC in sistemasDeFinanciamento else None
        
        return ResultadoCalculoFinanciamento(resultadoSac, resultadoPrice)
        
    def calcula_financiamento_price(self, valor_bem, taxa_juros, num_parcelas):
        linhas = []
        valor_parcelas = valor_bem*((((1+taxa_juros/100)**num_parcelas)*taxa_juros/100)/(((1+taxa_juros/100)**num_parcelas)-1))
        juros = valor_bem * (taxa_juros / 100)
        amortizacao = valor_parcelas - juros
        linhas.append([0, "", "", "", valor_bem])
        for i in range(1, num_parcelas + 1):
            juros = valor_bem * (taxa_juros / 100)
            amortizacao = (valor_parcelas - juros)
            valor_bem = valor_bem - amortizacao
            linhas.append([i, round(valor_parcelas, 2), round(amortizacao, 2), round(juros, 2), round(valor_bem, 2)])

        linhas[len(linhas) - 1][4] = 0
        linhas.append(["Total dos Pagamentos", sum([x[1] for x in linhas[1:]]), "", "", ""])
        return linhas

    def calcula_financiamento_sac(self, valor_bem, taxa_juros, num_parcelas):
        linhas = []
        amortizacao = valor_bem / num_parcelas
        linhas.append([0, "", "", "", valor_bem])
        for i in range(1, num_parcelas + 1):
            juros = valor_bem * (taxa_juros / 100)
            prestacao = juros + amortizacao
            valor_bem -= amortizacao
            linhas.append([i, round(prestacao, 2), round(amortizacao, 2), round(juros, 2), round(valor_bem, 2)])
        
        linhas[len(linhas) - 1][4] = 0
        linhas.append(["Total dos Pagamentos", sum([x[1] for x in linhas[1:]]), "", "", ""])
        return linhas
