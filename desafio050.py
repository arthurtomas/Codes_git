#Somador de Números Pares
rd = 0
soma = 0
for c in range(1, 7):
    num = int(input('Digite um número: '))
    rd = num % 2
    if rd == 0:
        soma = soma + num
print('Somando os números pares que foram digitados temos: {}'.format(soma))
