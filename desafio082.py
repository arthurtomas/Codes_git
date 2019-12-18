# Entrada dos valores da lista
numbers_list = []
lista_par = []
lista_impar = []
while True:
    ele = int(input('Digite um número: '))
    numbers_list.append(ele)
    saida = 'zerado'
# Verificação de saída
    while saida not in 'nNsS':
        saida = str(input('Você deseja continuar? [S/N]: '))
    if saida in 'nN':
        break
# Verificador de par ou ímpar
for c in range(0, len(numbers_list)):
    verificador_par = numbers_list[c] % 2
    if verificador_par == 0:
        lista_par.append(numbers_list[c])
    else:
        lista_impar.append(numbers_list[c])
# Saídas solicitadas
print('-=' * 30)
print(f'Lista original: {numbers_list}')
print(f'Lista em ordem crescente: {sorted(numbers_list)}')
print(f'Lista dos pares: {lista_par}')
print(f'Lista dos pares crescente: {sorted(lista_par)}')
print(f'Lista dos ímpares: {lista_impar}')
print(f'Lista dos ímpares crescente: {sorted(lista_impar)}')
print('-=' * 30)
