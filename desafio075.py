# Recebendo os valores das variáveis
print('-=' * 30)
a = int(input('Digite um número: '))
b = int(input('Digite um número: '))
c = int(input('Digite um número: '))
d = int(input('Digite um número: '))
tuple_numbers = (a, b, c, d)
count_even = 0
print('-=' * 30)
# Mostrando a ocorrência do número 9
if tuple_numbers.count(9) == 1:
    print(f'O número 9 apareceu {tuple_numbers.count(9)} vez.')
else:
    print(f'O número 9 apareceu {tuple_numbers.count(9)} vezes.')
# Mostrando a ocorrência do número 3 pela primeira vez
if 3 not in tuple_numbers:
    print('O número 3 não apareceu. ')
else:
    print(f'O número 3 apareceu pela primeira vez na {tuple_numbers.index(3) + 1}ª posição.')
# Contando a quantidade de números pares
for c in range(0, 4):
    even_number = tuple_numbers[c] % 2
    if even_number == 0:
        count_even += 1
print(f'A ocorrência de números pares foi igual a: {count_even}')
