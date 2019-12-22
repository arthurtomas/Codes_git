# Lista usada
matrix = [[], [], []]

# Laço de recebimento dos elementos da Matriz
for line in range(0, 3):
    for column in range(0, 3):
        ele = int(input(f'Digite o elemento {line}, {column}: '))
        matrix[line].append(ele)

# Impressão da Matriz formatada
print(matrix[0])
print(matrix[1])
print(matrix[2])

# Outra maneira de impressão
'''for line in range(0, 3):
    for column in range(0, 3):
        print(f'{matrix[line][column]:2}', end='')
    print('')'''
