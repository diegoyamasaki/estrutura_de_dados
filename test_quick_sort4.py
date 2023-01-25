import numpy as np


def particao(vetor, inicio, fim):
    pivo = vetor[fim]
    i = inicio - 1
    for j in range(inicio, fim):
        if vetor[j] <= pivo:
            i += 1
            vetor[i], vetor[j] = vetor[j], vetor[i]
    vetor[i + 1], vetor[fim] = vetor[fim], vetor[i + 1]
    return i + 1


def quick_sort(vetor, inicio, fim):
    if inicio < fim:
        posicao = particao(vetor, inicio, fim)

        quick_sort(vetor, inicio, posicao - 1)
        quick_sort(vetor, posicao + 1, fim)
    return vetor


if __name__ == '__main__':
    array = np.array([15, 34, 8, 3])
    print(quick_sort(array, 0, len(array) - 1))