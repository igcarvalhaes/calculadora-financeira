from enum import Enum

class FormatoInputCalculadoraFinanciamento(Enum):
    FORMATO_VALOR_DO_BEM = "^[1-9]\d{0,2}(\.\d{3})*,\d{2}$"
    FORMATO_TAXA_DE_JUROS = "[1-9]\d*"
    FORMATO_NUMERO_DE_PARCELAS = "[1-9]\d*"