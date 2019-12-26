# Dicionário e listas usadas
jogador = {}
gols = []
jogadores = []

# Entrada de dados
while True:
    jogador.clear()
    gols.clear()
    jogador['Nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    for c in range(0, partidas):
        gols.append(int(input(f'  Quantos gols na partida {c+1}? ')))
    jogador['Gols'] = gols[:]
    jogador['Total'] = sum(gols)
    jogadores.append(jogador.copy())
    continuar = 'clear'
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]: ')).upper()
    if continuar == 'N':
        break

# Impressão das informações gerais dos jogadores
print('-=' * 30)
c = 0
for jogador in jogadores:
    c += 1
    print(f'No.{c} Nome: {jogador["Nome"]} jogou {len(jogador["Gols"])} jogos e fez {jogador["Total"]} gols.')

# Solicitação de informações detalhadas do jogador
while True:
    print('-=' * 30)
    detalhes = int(input('Digite o número do jogador que deseja ver os detalhes (999 para sair): '))
    if detalhes == 999:
        break
    if detalhes <= len(jogadores):
        print(jogadores[detalhes-1])
    else:
        print('Digite uma opção válida!')
