def buscaMenor(array):
    menor = array[0]
    menor_indice = 0
    for i in range(1, len(array)):
        if array[i] < menor:
            menor = array[i]
            menor_indice = i
    return menor_indice


def ordenacao_por_selecao(array):
    novo_array = []
    for _ in range(len(array)):
        menor = buscaMenor(array)
        novo_array.append(array.pop(menor))
    return novo_array


print(ordenacao_por_selecao([5, 3, 6, 2, 10]))

