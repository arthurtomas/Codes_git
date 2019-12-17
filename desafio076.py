# Tupla completa
stuffs = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25, 'Transferidor', 4.2, 'Compasso', 9.99,
          'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34.9)
# Impressão da listagem de preços
print(' ' * 15, 'LISTA DE PREÇOS', ' ' * 15)
print('-=' * 25)
for c in range(0, len(stuffs), 2):
    print(f'{stuffs[c]:.<30} R$ {stuffs[c+1]:.2f}')
print('-=' * 25)
