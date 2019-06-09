from calculadorafinanceira.model.SistemaFinanciamento import SistemaFinanciamento

class CalculadoraFinanciamento:
    
    def calcula_financiamento(self, valor_bem, taxa_juros, num_parcelas, sistema_financiamento):
        if (sistema_financiamento is SistemaFinanciamento.PRICE):
            self.calcula_financiamento_price(valor_bem, taxa_juros, num_parcelas, sistema_financiamento)
        elif (sistema_financiamento is SistemaFinanciamento.SAC):
            self.calcula_financiamento_sac(valor_bem, taxa_juros, num_parcelas, sistema_financiamento)
        
    def calcula_financiamento_price(self, valor_bem, taxa_juros, num_parcelas, sistema_financiamento):
        amortizacao = valor_bem / num_parcelas
	    tabelaSac = [[0 for x in range(5)] for y in range(num_parcelas+1)]
	    for i in range(0,num_parcelas+1):
	        juros = valor_bem * (taxa_juros / 100)
	        prestacao = juros + amortizacao
	        if i==0:
	            valor_bem=valor_bem
	            tabelaSac[i][0]=i
	            tabelaSac[i][1]=0
	            tabelaSac[i][2]=0
	            tabelaSac[i][3]=0
	            tabelaSac[i][4]=(valor_bem) 
	        else: 
	            valor_bem = valor_bem - amortizacao
	            tabelaSac[i][0]=i
	            tabelaSac[i][1]=(prestacao)
	            tabelaSac[i][2]=(amortizacao)
	            tabelaSac[i][3]=(juros)
	            tabelaSac[i][4]=(valor_bem) 
	    print(tabelaSac)

    def calcula_financiamento_sac(self, valor_bem, taxa_juros, num_parcelas, sistema_financiamento):
        valor_parcelas= valor_bem*((((1+taxa_juros/100)**num_parcelas)*taxa_juros/100)/(((1+taxa_juros/100)**num_parcelas)-1));
		amortizacao=valor_parcelas-juros;
		tabelaPrice = [[0 for x in range(5)] for y in range(num_parcelas+1)]
		print(cabecalho)
		for i in range(0,num_parcelas+1):
		    if i==0:                                              						#Esse if é só para imprimir o valor do bem quando não há parcela nenhuma ainda. 
		        tabelaPrice[i][0]=i
		        tabelaPrice[i][1]=(0)
		        tabelaPrice[i][2]=(0)
		        tabelaPrice[i][3]=(0)
		        tabelaPrice[i][4]=(valor_bem)
		    else:
		        if i==0:
		           valor_bem=valor_bem
		        else:
		           valor_bem=tabelaPrice[i-1][4]
		           juros=valor_bem*(taxa_juros/100)
		           amortizacao=valor_parcelas-juros
		           
		        tabelaPrice[i][0]=i
		        tabelaPrice[i][1]=(valor_parcelas)
		        tabelaPrice[i][2]=(amortizacao)
		        tabelaPrice[i][3]=(juros)                                               #valor do juros em reais
		        if (valor_bem*(1+(taxa_juros/100))**(1)-valor_parcelas<10**(-2)):
		            tabelaPrice[i][4]=(0)
		        else:
		            tabelaPrice[i][4]=(valor_bem*(1+(taxa_juros/100))**(1)-valor_parcelas)  
		print(tabelaPrice)