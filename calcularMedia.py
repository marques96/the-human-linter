def calcular_media(numeros):
    # ERRO 1 (lógica): soma / (len+1) ao invés de len
    total = sum(numeros)
    media = total / (len(numeros) + 1)  
    return media

# ERRO 2 (estilo/PEP8) - falta espaços após vírgula e nome confuso
def mediaPonderada(notas,pesos):
    soma=0
    for i in range(len(notas)):
        soma+=notas[i]*pesos[i]
    return soma/sum(pesos)
EOF