import numpy as np


class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

    def mostra_no(self):
        print(self.valor)


class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None
        self.ligacoes = []

    def inserir(self, valor):
        novo = No(valor)

        if not self.raiz:
            self.raiz = novo
        else:
            atual = self.raiz
            while True:
                pai = atual
                if valor < atual.valor:
                    # Vai para esquerda (menor que o pai)
                    atual = atual.esquerda
                    if not atual:
                        pai.esquerda = novo
                        self.ligacoes.append(str(pai.valor) + '->' + str(novo.valor))
                        return
                else:
                    # Vai para direita (maior que o pai)
                    atual = atual.direita
                    if not atual:
                        pai.direita = novo
                        self.ligacoes.append(str(pai.valor) + '->' + str(novo.valor))
                        return

    def pesquisar(self, valor):
        atual = self.raiz
        while atual.valor != valor:
            if valor < atual.valor:
                atual = atual.esquerda
            else:
                atual = atual.direita
            if not atual:
                return None
        return atual


if __name__ == '__main__':
    arvore = ArvoreBinariaBusca()
    arvore.inserir(53)
    arvore.inserir(30)
    arvore.inserir(14)
    arvore.inserir(39)
    arvore.inserir(9)
    arvore.inserir(23)
    arvore.inserir(34)
    arvore.inserir(49)
    arvore.inserir(72)
    arvore.inserir(61)
    arvore.inserir(84)
    arvore.inserir(79)
    print('PESQUISAR :: ', arvore.pesquisar(99))


