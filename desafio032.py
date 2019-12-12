year = int(input('Digite o ano: '))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('{} é Bissexto!'.format(year))
else:
    print('{} não é Bissexto!'.format(year))
