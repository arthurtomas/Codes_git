from random import randrange
user_choice = 0
par_impar = ''
soma = 0
count_victory = 0
while True:
    pc_choice = randrange(0, 11)
    print('-=' *20)
    user_choice = int(input('Que número você escolhe? '))
    par_impar = str(input('Você escolhe par ou impar? [P/I]: ')).upper()
    while par_impar not in 'PI':
        par_impar = str(input('Você escolhe par ou impar? [P/I]: ')).upper()
    soma = (user_choice + pc_choice) % 2
    if par_impar == 'P' and soma == 0:
        print(f'{user_choice} + {pc_choice} = {user_choice + pc_choice}. Parabéns, você ganhou!')
        count_victory += 1
    elif par_impar == 'I' and soma != 0:
        print(f'{user_choice} + {pc_choice} = {user_choice + pc_choice}. Parabéns, você ganhou!')
        count_victory += 1
    else:
        print(f'Errou! {user_choice} + {pc_choice} = {user_choice + pc_choice} não é: {par_impar}')
        break
print(f'Você conseguiu ganhar {count_victory} vezes do computador.')