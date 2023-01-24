import numpy as np


def select_sort(vetor):
    for i in range(len(vetor)):
        posicao = i
        for j in range(i+1, len(vetor)):
            if vetor[posicao] > vetor[j]:
                posicao = j
        temp = vetor[i]
        vetor[i] = vetor[posicao]
        vetor[posicao] = temp
    return vetor



def particao(vetor, inicio, final):
    pivo = vetor[final]
    i = inicio - 1
    for j in range(inicio, final):
        if vetor[j] <= pivo:
            i += 1
            vetor[i], vetor[j] = vetor[j], vetor[i]
    vetor[i+1], vetor[final] = vetor[final], vetor[i+1]
    return i + 1


def quick_sort(vetor, inicio, final):
    if inicio < final:
        posicao = particao(vetor, inicio, final)

        # sort vetor da esquerda
        quick_sort(vetor, inicio, posicao - 1)

        # sort vetor da direita
        quick_sort(vetor, posicao + 1, final)
    return vetor


# print(select_sort(np.array([15, 34, 8, 3])))

array = np.array([15, 34, 8, 3])
print(quick_sort(array, 0, len(array) - 1))


