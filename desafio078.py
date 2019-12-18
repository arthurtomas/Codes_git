# Recebimento de valores da lista
lista =[]
for c in range(0, 5):
    lista.append(int(input(f'Digite o número da posição {c}: ')))
# Impressão dos dados solicitados
print(f'O maior valor nessa lista é: {max(lista)} que está na posição {lista.index(max(lista))}')
print(f'O menor valor dessa lista é: {min(lista)} que está na posição {lista.index(min(lista))}')
