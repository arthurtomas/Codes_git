print('Para sair digite um número negativo: ')
while True:
    n = int(input('Digite um número: '))
    if n < 0:
        print('Saindo...')
        break
    for c in range(1, 11):
        print(f'{n:2} x {c:2} = {n*c}')
    print('')
