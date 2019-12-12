#Analisador de Números Primos
num = int(input('Digite um número: '))
if num == 2:
    print('{} é primo!'.format(num))
elif num == 1 or num == 0:
    print('{} não é primo!'.format(num))
for c in range(2, num):
    if (num % c) == 0:
        print('{} não é primo, porque também é divisível por {}!'.format(num, c))
        break
    elif c == num-1:
        print('{} é primo!'.format(num))
