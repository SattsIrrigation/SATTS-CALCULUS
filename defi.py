def calcular_ini(umidade, chuva):
    return 100 - ((0.7 * umidade) + (0.3 * chuva))

def classificar_ini(ini):
    if ini <= 30:
        return "BOA"
    elif ini <= 60:
        return "ATENCAO"
    else:
        return "IRRIGAR"