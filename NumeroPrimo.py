from sys import exit
divisores = 0
n = int(input('Digite um número para verificarmos se ele é primo: '))
if n < 0:
    print('Por favor, digite um número maior que zero.')
    exit()
for c in range(1, n + 1):
    if n % c == 0:
        divisores += 1
if divisores == 2:
    print('{} é primo!'.format(n))
else:
    print('{} não é primo!'.format(n))
