preco_total = 0
count_1k_mais = 0
menor_preco = 100000000000
produto_mais_barato = ''
while True:
    print('-=' * 30)
    nome_produto = str(input('Nome do produto: ')).strip()
    preco = float(input('Preço: R$ '))
    preco_total += preco
    if preco > 1000:
        count_1k_mais += 1
    if preco < menor_preco:
        menor_preco = preco
        produto_mais_barato = nome_produto
    continuar = 'zerado'
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]: ')).upper()
    if continuar == 'N':
        break
print('-=' * 30)
print(f'Valor total: R$ {preco_total:.2f}')
print(f'{count_1k_mais} produtos custaram mais que R$ 1000,00')
print(f'Nome do produto mais barato: {produto_mais_barato}')
print(f'Preço do produto mais barato: R$ {menor_preco:.2f}')
