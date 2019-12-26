from time import sleep


def contador():

    print('-=' * 30)
    print('De 1 até 10, de 1 em 1:')
    for c in range(1, 11):
        sleep(0.3)
        print(f'{c}...', end='')
    print('FIM')

    print('-=' * 30)
    print('De 10 até 0, de 2 em 2:')
    for c in range(10, -1, -2):
        sleep(0.3)
        print(f'{c}...', end='')
    print('FIM')

    print('-=' * 30)
    print('Agora é sua vez de personalizar a contagem!')
    inicio = int(input('Início: '))
    fim = int(input('Fim: '))
    intervalo = int(input('Intervalo: '))
    print('-=' * 30)
    print(f'Contagem de {inicio} até {fim}, de {intervalo} em {intervalo}:')

    if inicio < fim:
        for c in range(inicio, fim+1, intervalo):
            sleep(0.3)
            print(f'{c}...', end='')
        print('FIM')

    elif (inicio > fim) and (intervalo > 0):
        intervalo = intervalo * -1
        for c in range(inicio, fim - 1, intervalo):
            sleep(0.3)
            print(f'{c}...', end='')
        print('FIM')

    elif (inicio > fim) and (intervalo < 0):
        for c in range(inicio, fim - 1, intervalo):
            sleep(0.3)
            print(f'{c}...', end='')
        print('FIM')

    elif intervalo == 0:
        print(f'Impossível se chegar de {inicio} até {fim} de 0 em 0!')


contador()
