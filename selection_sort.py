import numpy as np


def selection_sort(vetor):
    n = len(vetor)
    for i in range(n):
        posicao = i
        for j in range(i + 1, n):
            if vetor[posicao] > vetor[j]:
                posicao = j
        tmp = vetor[i]
        vetor[i] = vetor[posicao]
        vetor[posicao] = tmp
    return vetor


print(selection_sort(np.array([15, 34, 8, 3])))

print(selection_sort(np.array([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])))
