from random import choice
from time import sleep
jokenpo = ['Pedra', 'Papel', 'Tesoura']
escolha = int(input('\033[1;30m'
                    '1. Pedra\n'
                    '2. Papel\n'
                    '3. Tesoura\033[m\n'
                    'Qual a sua escolha? '))
print("\n\033[1;30mJO...")
sleep(1)
print("KEN...")
sleep(1)
print("POOH!!!\033[m\n")
mescolha = choice(jokenpo)
if escolha == 1:
    if mescolha == 'Pedra':
        print('Pedra x {}. Você empatou!'.format(mescolha))
    elif mescolha == 'Papel':
        print('Pedra x {}. Você perdeu!'.format(mescolha))
    elif mescolha == 'Tesoura':
        print('Pedra x {}. Você ganhou!'.format(mescolha))
    else:
        print('Opção Inválida!')
elif escolha == 2:
    if mescolha == 'Pedra':
        print('Papel x {}. Você ganhou!'.format(mescolha))
    elif mescolha == 'Papel':
        print('Papel x {}. Você empatou!'.format(mescolha))
    elif mescolha == 'Tesoura':
        print('Papel x {}. Você perdeu!'.format(mescolha))
    else:
        print('Opção Inválida!')
elif escolha == 3:
    if mescolha == 'Pedra':
        print('Tesoura x {}. Você perdeu!'.format(mescolha))
    elif mescolha == 'Papel':
        print('Tesoura x {}. Você ganhou!'.format(mescolha))
    elif mescolha == 'Tesoura':
        print('Tesoura x {}. Você empatou!'.format(mescolha))
    else:
        print('Opção Inválida!')
else:
    print('Opção Inválida!')
