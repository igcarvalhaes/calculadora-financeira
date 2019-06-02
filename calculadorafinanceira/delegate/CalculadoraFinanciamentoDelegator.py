from calculadorafinanceira.model.CalculadoraFinanciamento import CalculadoraFinanciamento

class CalculadoraFinanciamentoDelegator:
    
    def calcula_financiamento(self, valor_bem, taxa_juros, num_parcelas, sistema_financiamento):
        # TODO: Fazer uma verificacao dos dados da simulacao
        # Se tiver algum erro indicar pro usuario o campo com erro
        
        return CalculadoraFinanciamento.calcula_financiamento(valor_bem=valor_bem, taxa_juros=taxa_juros, num_parcelas=num_parcelas, sistema_financiamento=sistema_financiamento)