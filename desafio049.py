#Tabuada
n = int(input('Digite um número para ver sua Tabuada: '))
for c in range(1, 11):
    print('{}x{:2} = {}'.format(n, c, n * c))
