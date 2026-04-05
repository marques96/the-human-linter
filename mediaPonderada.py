def mediaPonderada(notas,pesos):
    soma=0
    for i in range(len(notas)):
        soma+=notas[i]*pesos[i]
    return soma/sum(pesos)