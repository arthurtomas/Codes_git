# Entrada dos valores da lista
numbers_list = []
while True:
    ele = int(input('Digite um número: '))
    if ele in numbers_list:
        print('Esse número já se encontra na lista')
    else:
        numbers_list.append(ele)
    saida = 'zerado'
# Verificação de saída
    while saida not in 'nNsS':
        saida = str(input('Você deseja continuar? [S/N]: '))
    if saida in 'nN':
        break
# Impressão da lista ordenada em ordem crescente
numbers_list.sort()
print(f'Lista em ordem crescente: {numbers_list}')

