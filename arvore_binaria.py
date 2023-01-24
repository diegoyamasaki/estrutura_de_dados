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

    # Raiz, esquerda, direita
    def pre_ordem(self, no):
        if no:
            print(no.valor)
            self.pre_ordem(no.esquerda)
            self.pre_ordem(no.direita)

    # Esquerda, raiz, direita
    def em_ordem(self, no):
        if no:
            self.em_ordem(no.esquerda)
            print(no.valor)
            self.em_ordem(no.direita)

    # Esquerda, direita, raiz
    def pos_ordem(self, no):
        if no:
            self.pos_ordem(no.esquerda)
            self.pos_ordem(no.direita)
            print(no.valor)

    def exclusao(self, valor):
        if not self.raiz:
            print('A Arvore está vazia')
            return
        atual = self.raiz
        pai = self.raiz
        e_esquerda = True
        while atual.valor != valor:
            pai = atual
            if valor < atual.valor:
                e_esquerda = True
                atual = atual.esquerda
            else:
                e_esquerda = False
                atual = atual.direita
            if not atual:
                return False
        # O nó é uma folha (nao tem esquerda nem direita)
        if not atual.esquerda and not atual.direita:
            if atual == self.raiz:
                self.raiz = None
            elif e_esquerda:
                self.ligacoes.remove(f'{pai.valor}->{atual.valor}')
                pai.esquerda = None
            else:
                self.ligacoes.remove(f'{pai.valor}->{atual.valor}')
                pai.direita = None
        # o nó a ser apagado nao possui filho na direita
        elif not atual.direita:
            if atual == self.raiz:
                self.raiz = atual.esquerda
            elif e_esquerda:
                self.ligacoes.remove(f'{pai.valor}->{atual.esquerda.valor}')
                pai.esquerda = atual.esquerda
            else:
                self.ligacoes.remove(f'{pai.valor}->{atual.esquerda.valor}')
                pai.direita = atual.esquerda
        elif not atual.esquerda:
            if atual == self.raiz:
                self.raiz = atual.direita
            elif e_esquerda:
                self.ligacoes.remove(f'{pai.valor}->{atual.direita.valor}')
                pai.esquerda = atual.direita
            else:
                self.ligacoes.remove(f'{pai.valor}->{atual.direita.valor}')
                pai.direita = atual.direita
        else:
            # O nó possui dois filhos
            sucessor = self.get_sucessor(atual)

            if atual == self.raiz:
                self.raiz = sucessor
            elif e_esquerda:
                pai.esquerda = sucessor
            else:
                pai.direita = sucessor
            sucessor.esquerda = atual.esquerda
        return True

    def get_sucessor(self, no):
        pai_sucessor = no
        sucessor = no
        atual = no.direita
        while atual != None:
            pai_sucessor = sucessor
            sucessor = atual
            atual = atual.esquerda
        if sucessor != no.direita:
            pai_sucessor.esquerda = sucessor.direita
            sucessor.direita = no.direita
        return sucessor


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
    # print('PESQUISAR :: ', arvore.pesquisar(99))

    # arvore.pre_ordem(arvore.raiz)
    # arvore.em_ordem(arvore.raiz)
    # arvore.pos_ordem(arvore.raiz)
    arvore.exclusao(53)
    # arvore.ligacoes.remove('14->9')
    print(arvore.raiz.valor)



