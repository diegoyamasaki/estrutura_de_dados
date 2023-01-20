class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        self.anterior = None

    def mostra_no(self):
        print(self.valor)


class ListaDuplamenteEncadeadas:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def __lista_vazia(self):
        return self.primeiro == None

    def insere_inicio(self, valor):
        novo = No(valor)
        if self.__lista_vazia():
            self.ultimo = novo
        else:
            self.primeiro.anterior = novo
        novo.proximo = self.primeiro
        self.primeiro = novo

    def insere_final(self, valor):
        novo = No(valor)
        if self.__lista_vazia():
            self.primeiro = novo
        else:
            self.ultimo.proximo = novo
            novo.anterior = self.ultimo
        self.ultimo = novo

    def excluir_inicio(self):
        temp = self.primeiro
        if not self.primeiro.proximo:
            self.ultimo = None
        else:
            self.primeiro.proximo.anterior = None
        self.primeiro = self.primeiro.proximo
        return temp

    def excluir_final(self):
        temp = self.ultimo
        if not self.primeiro.proximo:
            self.primeiro = None
        else:
            self.ultimo.anterior.proximo = None
        self.ultimo = self.ultimo.anterior
        return temp

    def excluir_posicao(self, valor):
        if self.__lista_vazia():
            return None
        atual = self.primeiro
        while atual.valor != valor:
            atual = atual.proximo
            if not atual:
                return None
        if atual == self.primeiro:
            self.primeiro = atual.proximo
        else:
            atual.anterior.proximo = atual.proximo

        if atual == self.ultimo:
            self.ultimo = atual.anterior
        else:
            atual.proximo.anterior = atual.anterior

    def mostrar_frente(self):
        atual = self.primeiro
        while atual:
            atual.mostra_no()
            atual = atual.proximo

    def mostrar_tras(self):
        atual = self.ultimo
        while atual:
            atual.mostra_no()
            atual = atual.anterior


if __name__ == '__main__':
    lista = ListaDuplamenteEncadeadas()
    lista.insere_inicio(1)
    lista.insere_inicio(2)
    # lista.insere_inicio(3)
    # lista.insere_inicio(4)
    # lista.insere_inicio(5)
    # lista.mostrar_frente()
    # print('mostrar tras')
    # lista.mostrar_tras()
    lista.insere_final(3)
    lista.insere_final(4)
    lista.mostrar_frente()
    print()
    # lista.mostrar_tras()
    # print('excluir inicio')
    # lista.excluir_inicio()
    # lista.mostrar_frente()
    # print('excluir final')
    # lista.excluir_final()
    # lista.mostrar_frente()
    lista.excluir_posicao(3)
    lista.mostrar_frente()
    print()
    lista.mostrar_tras()
    lista.excluir_posicao(4)
    print()
    lista.mostrar_frente()
    print()
    lista.excluir_posicao(1)
    lista.mostrar_frente()

