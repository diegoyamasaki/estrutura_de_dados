def regressiva(i):
    print(i)
    if i <= 1:
        return
    else:
        regressiva(i - 1)

# regressiva(10)


def fatorial(x):
    if x == 1:
        return 1
    else:
        return x * fatorial(x - 1)


#fatoria 1 = 1
#fatorial 2 = 2 * 1
#fatorial 3 = 3 *2
# print(fatorial(3))


# fatorial 1        = 1
# fatorial 2 2 * 1  = 2
# fatorial 3 3 * 2  = 16
# fatorial 4 4 * 6  = 24
# fatorial 5 5 * 24 = 120
print(fatorial(5))

