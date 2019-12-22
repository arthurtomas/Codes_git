# Listas usada
matrix = [[], [], []]
even = []
column_3 = []

# Laço de recebimento dos elementos da Matriz
for line in range(0, 3):
    for column in range(0, 3):
        ele = int(input(f'Digite o elemento {line}, {column}: '))
        matrix[line].append(ele)

# Criação da lista dos pares
for line in range(0, 3):
    for column in range(0, 3):
        if (matrix[line][column] % 2) == 0:
            even.append(matrix[line][column])

# Criação da lista dos elementos da coluna 3
for line in range(0, 3):
    column_3.append(matrix[line][2])

# Saída dos dados solicitados

# Impressão da Matriz formatada
print('-=' * 30)
print('Matriz 3x3:')
print(matrix[0])
print(matrix[1])
print(matrix[2])

# Impressão dos valores pares
print('-=' * 30)
print(f'Valores pares: {even}')
print(f'Soma dos valores pares: {sum(even)}')

# Impressão dos valores da terceira coluna
print('-=' * 30)
print(f'Valores da terceira coluna: {column_3}')
print(f'Soma dos valores da terceira coluna: {sum(column_3)}')

# Impressão do maior valor da segunda linha
print('-=' * 30)
print(f'Segunda linha: {matrix[1]}')
print(f'Maior valor da segunda linha: {max(matrix[1])}')
