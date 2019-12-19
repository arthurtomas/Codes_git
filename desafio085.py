# Listas necessárias
numbers =[]
even = []
odd = []

# Entrada e análise de dados
print('-=' * 7, 'ENTRADA DE DADOS', '-=' * 7)
for c in range(1, 8):
    num = int(input(f'{c}° número: '))
    if (num % 2) == 0:
        even.append(num)
    else:
        odd.append(num)

# Organização e saída de dados
numbers.append(even)
numbers.append(odd)
print('-=' * 30)
print(f'Lista inteira com pares e ímpares: {numbers}')
print(f'Lista dos pares em ordem crescente: {sorted(numbers[0])}')
print(f'Lista dos ímpares em ordem crescente: {sorted(numbers[1])}')
print('-=' * 30)
