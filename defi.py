import math

def calcular_umidade_exponencial(umidade_inicial, taxa_evaporacao, tempo):
    """
    Calcula a umidade do solo ao longo do tempo usando decaimento exponencial.
    U(t) = U0 * e^(-k*t)
    """
    return umidade_inicial * math.exp(-taxa_evaporacao * tempo)

def classificar_status(umidade_atual, limite_critico=30):
    """
    Classifica se precisa irrigar baseado no limite crítico.
    """
    if umidade_atual <= limite_critico:
        return "IRRIGAR"
    elif umidade_atual <= limite_critico + 20:
        return "ATENCAO"
    else:
        return "BOA"