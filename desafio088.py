# Importações
from random import randint
from time import sleep

# Lista usada
guess = []

# Entrada, geração e saída de dados
games = int(input('Digite quantos jogos deseja gerar: '))
print('PALPITES DA MEGA SENA:')
for games in range(0, games):
    while len(guess) != 6:
        num = randint(1, 61)
        if num not in guess:
            guess.append(num)
    print(f'Palpite {games + 1:2} = {sorted(guess)}')
    guess.clear()
    sleep(0.5)
