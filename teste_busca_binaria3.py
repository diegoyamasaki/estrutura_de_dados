def busca_binaria(lista, item):
    inicio = 0
    final = len(lista) - 1
    while inicio <= final:
        meio = (inicio + final) // 2
        chute = lista[meio]
        if chute == item:
            return chute

        if chute > item:
            final = meio - 1
        else:
            inicio = meio + 1
    return None


minha_lista = [1, 3, 5, 7, 9]

print(busca_binaria(minha_lista, 3))
print(busca_binaria(minha_lista, -1))

