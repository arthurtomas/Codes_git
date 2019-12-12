n = int(input('Digite quantos elementos da Sequência de Fibonacci você deseja ver: '))
ultimo = 1
penultimo = 1
count = 3
if n == 1:
    print('  1º Termo = 1')
elif n == 2:
    print('  1º Termo = 1')
    print('  2º Termo = 1')
else:
    print('  1º Termo = 1')
    print('  2º Termo = 1')
    while n >= count:
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        print('{:3}º Termo = {}'.format(count, termo))
        count += 1
