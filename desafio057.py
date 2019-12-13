gender = ' '
while gender not in 'MF':
    gender = str(input('Digite seu sexo [M/F]: ')).upper().strip()
    if gender in 'MF':
        print('Você é: \033[1;30m{}\033[m'.format(gender))
    else:
        print('\033[1;30m{}\033[m não é um sexo válido, por favor tente novamente.'.format(gender))
