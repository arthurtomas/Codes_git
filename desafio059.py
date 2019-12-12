choose = 0
while choose != 5:
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))
    choose = int(input('O que voce deseja fazer?\n'
          '[1] Somar\n'
          '[2] Multiplicar\n'
          '[3] Maior\n'
          '[4] Digitar novos números\n'
          '[5] Sair\n:'))
    if choose == 1:
        print('{} + {} = {}'.format(n1, n2, n1 + n2))
    elif choose == 2:
        print('{} x {} = {}'.format(n1, n2, n1 * n2))
    elif choose == 3:
        if n1 > n2:
            print('{} é maior que {}.'.format(n1, n2))
        else:
            print('{} é maior que {}.'.format(n2, n1))
    elif choose == 4:
        print('Ok')
    elif choose == 5:
        print('Saindo...')
    else:
        print('Você não digitou uma opção válida. Tente novamente.')
    print('')
