classificacao = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athetico-PR', 'São Paulo', 'Internacional',
                 'Corinthias', 'Fortaleza', 'Goiás', 'Bahia', 'Vasco da Gama', 'Atlético-MG', 'Fluminense',
                 'Botafogo', 'Ceará SC', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')
print('-=' * 30)
print('Os 5 primeiros colocados:')
for c in range(0, 5):
    print(f'{c+1}º colocado: {classificacao[c]}')
print('-=' * 30)
print('Os 4 últimos colocados:')
for c in range(16, 20):
    print(f'{c+1}º colocado: {classificacao[c]}')
print('-=' * 30)
print('Os times em ordem alfabética: ')
print(sorted(classificacao))
