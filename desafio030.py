num = int(input('Digite um número inteiro: '))
rest = num % 2
if rest == 0:
    print('{} é par.'.format(num))
else:
    print('{} é impar.'.format(num))
