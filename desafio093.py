# Dicionário e lista usada
jogador = {}
gols = []

# Entrada de dados e geração do dicionário
jogador['Nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
for c in range(0, partidas):
    gols.append(int(input(f'  Quantos gols na partida {c}? ')))
jogador['Gols'] = gols[:]
jogador['Total'] = sum(gols)

# Saída de dados
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'{k} tem valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["Nome"]} jogou {partidas} partidas.')
for c in range(0, partidas):
    print(f'  =>Na {c}ª partida, fez {gols[c]} gol(s)')
print(f'Totalizando {jogador["Total"]} gol(s)')
