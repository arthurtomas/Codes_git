divisores = 0
n = int(input('Digite um número para verificarmos se ele é primo: '))
for c in range(1, n + 1):
    if n % c == 0:
        divisores += 1
if divisores == 2:
    print('{} é primo!'.format(n))
else:
    print('{} não é primo!'.format(n))