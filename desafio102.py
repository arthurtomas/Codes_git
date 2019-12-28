def verificador():
    mostrar = str(input('Deseja mostrar o cálculo? [S/N]: '))
    if mostrar in 'Ss':
        return 'S'
    elif mostrar in 'Nn':
        return 'N'
    else:
        return verificador()


def fatorial(num, show):
    """
    -> Calcula o fatorial de um número
    :param num: Número para ser calculado
    :param show: Se mostra ou não o processo do cálculo
    :return: fatorial
    """
    f = 1
    if show in 'Ss':
        for c in range(num, 0, -1):
            if c > 1:
                print(f'{c} x ', end='')
                f *= c
        print(f'1 = {f}')
    elif show in 'Nn':
        for c in range(num, 0, -1):
            f *= c
        print(f'Fatorial de {num} = {f}')
    else:
        verificador()


num = int(input('Digite um número para ver seu Fatorial: '))
fatorial(num, verificador())




