bank_name = 'Banco Barzilay'
print('=' * 30)
print(f'{bank_name:^30}')
print('=' * 30)
print('\nNotas disponíveis:\n'
      'R$ 50\n'
      'R$ 20\n'
      'R$ 10\n'
      'R$ 1\n')
print('=' * 30)
valor = int(input('Digite o valor que deseja sacar: R$ '))
count_50 = valor // 50
valor = valor % 50
if count_50 != 0:
    print(f'Notas de R$ 50: {count_50}')
count_20 = valor // 20
valor = valor % 20
if count_20 != 0:
    print(f'Notas de R$ 20: {count_20}')
count_10 = valor // 10
valor = valor % 10
if count_10 != 0:
    print(f'Notas de R$ 10: {count_10}')
count_01 = valor // 1
valor = valor % 1
if count_01 != 0:
    print(f'Notas de R$ 1: {count_01}')
