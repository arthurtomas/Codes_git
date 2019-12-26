from random import randint
numeros = []


def sorteia():
    print('-=' * 30)
    for c in range(0, 5):
        num = randint(0, 9)
        numeros.append(num)
    print(f'Números sorteados: {numeros}')


def somapar():
    pares = 0
    for v in numeros:
        if (v % 2) == 0:
            pares += v
    print(f'Soma dos valores pares da lista sorteada: {pares}')


sorteia()
somapar()
