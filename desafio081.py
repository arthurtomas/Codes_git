# Entrada dos valores da lista
numbers_list = []
while True:
    ele = int(input('Digite um número: '))
    numbers_list.append(ele)
    saida = 'zerado'
# Verificação de saída
    while saida not in 'nNsS':
        saida = str(input('Você deseja continuar? [S/N]: '))
    if saida in 'nN':
        break
# Saídas solicitadas
print('-=' * 30)
print(f'Foram digitados {len(numbers_list)} números na lista.')
numbers_list.sort(reverse=True)
print(f'Lista em ordem decrescente: {numbers_list}')
if 5 in numbers_list:
    print('O número 5 se encontra na lista.')
else:
    print('O número 5 não se encontra na lista.')
print('-=' * 30)