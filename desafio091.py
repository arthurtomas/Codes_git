# Bibliotecas importadas
from random import randint
from operator import itemgetter
from time import sleep

# Definição randômica dos números dos dados
jogadas = {'jogador_1': randint(1, 6),
           'jogador_2': randint(1, 6),
           'jogador_3': randint(1, 6),
           'jogador_4': randint(1, 6)}

# Impressão dos valores em ordem de jogada
print('========JOGADAS=======')
for jogador, jogada in jogadas.items():
    sleep(1)
    print(f'{jogador} tirou {jogada} no dado.')

# Criação de Ranking e definção de contador igual a zero
ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)
c = 0

# Impressão do Ranking em ordem
print('\n========RANKING=======')
for jogador, jogada in ranking:
    c += 1
    sleep(1)
    print(f'{c}º Lugar: {jogador} que tirou {jogada}')

