#Maior de idade ou não
count = 0
for c in range(0, 7):
    birth = int(input('{}. Digite o ano de nascimento: '.format(c+1)))
    age = 2019 - birth
    if age >= 18:
        count = count + 1
print('Levando em consideração os anos digitados, temos {} maiores de idade e {} menores.'.format(count, 7 - count))
