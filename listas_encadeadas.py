import numpy as np


class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

    def mostra_no(self):
        print(self.valor)


class ListaEncadeada:
    def __init__(self):
        self.primeiro = None

    def insere_inicio(self, valor):
        novo = No(valor)
        novo.proximo = self.primeiro
        self.primeiro = novo

    def mostrar(self):
        if not self.primeiro:
            print('Lista esta vazia')
            return
        atual: No = self.primeiro
        while atual:
            atual.mostra_no()
            atual = atual.proximo

    def pesquia(self, valor):
        if not self.primeiro:
            print('Lista esta vazia')
            return
        atual = self.primeiro
        while atual.valor != valor:
            if not atual.proximo:
                return None
            else:
                atual = atual.proximo
        return atual

    def excluir_inicio(self):
        if not self.primeiro:
            return None
        tmp = self.primeiro
        self.primeiro = self.primeiro.proximo
        return tmp

    def excluir_posicao(self, valor):
        if not self.primeiro:
            return None
        atual = self.primeiro
        anterior = self.primeiro
        while atual.valor != valor:
            if not atual.proximo:
                return None
            anterior = atual
            atual = atual.proximo
        if atual == self.primeiro:
            self.primeiro = self.primeiro.proximo
        else:
            anterior.proximo = atual.proximo
        return atual

if __name__ == '__main__':
    lista_encadeada = ListaEncadeada()
    lista_encadeada.insere_inicio(1)
    lista_encadeada.insere_inicio(2)
    lista_encadeada.insere_inicio(3)
    lista_encadeada.insere_inicio(4)
    lista_encadeada.insere_inicio(5)
    lista_encadeada.mostrar()
    # print('Excluindo do inicio')
    # lista_encadeada.excluir_inicio()
    # lista_encadeada.excluir_inicio()
    # lista_encadeada.excluir_inicio()
    # lista_encadeada.excluir_inicio()
    # lista_encadeada.excluir_inicio()
    # lista_encadeada.excluir_inicio()
    # lista_encadeada.excluir_inicio()
    # lista_encadeada.mostrar()
    # pesquisa = lista_encadeada.pesquia(3)
    # if pesquisa:
    #     print('Encontrado: ', pesquisa.valor)
    # else:
    #     print("Nao encontrado")
    print('Excluir posição')
    lista_encadeada.excluir_posicao(3)
    lista_encadeada.excluir_posicao(1)
    lista_encadeada.excluir_posicao(5)
    lista_encadeada.mostrar()



