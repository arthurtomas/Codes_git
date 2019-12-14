count_man = 0
count_18_mais = 0
count_woman_20_menos = 0
while True:
    print('-=' * 30)
    age = int(input('Idade: '))
    gender = 'zerado'
    while gender not in 'MF':
        gender = str(input('Sexo [M/F]: ')).upper()
    choice = 'zerado'
    while choice not in 'SN':
        choice = str(input('Deseja continuar? [S/N]: ')).upper()
    if age > 18:
        count_18_mais += 1
    if gender == 'M':
        count_man += 1
    if gender == 'F' and age < 20:
        count_woman_20_menos += 1
    if choice == 'N':
        break
print('-=' * 30)
print(f'{count_18_mais} pessoas têm mais de 18 anos.')
print(f'Foram cadastrados {count_man} homens.')
print(f'Foram cadastradas {count_woman_20_menos} mulheres com menos de 20 anos.')


