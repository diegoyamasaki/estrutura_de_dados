import timeit


def teste_for():
    for _ in range(5):
        print('Recursão')


def recursao(i: int = 0):
    print('Recursão')
    i += 1
    if i == 5:
        return
    return recursao(i)


def soma1(n):
    soma = 0
    for i in range(n + 1):
        soma += i
    return soma


def soma2(n):
    if n == 0:
        return 0
    return n + soma2(n - 1)


def fatorial(m):
    if m <= 1:
        return 1
    return m * fatorial(m - 1)


def potencia(base, expoente):
    if expoente == 0:
        return 1
    return base * potencia(base, expoente - 1)


if __name__ == '__main__':
    # print(soma1(5))
    # print(soma2(5))
    # print(5+4+3+2+1+0)
    # print(fatorial(0))
    print(potencia(2, 3))
