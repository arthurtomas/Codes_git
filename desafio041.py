birth = int(input('Digite o ano do seu nascimento: '))
age = 2019 - birth
if age <= 9:
    print('Você tem {} anos sua categoria é MIRIM!'.format(age))
elif age <= 14:
    print('Você tem {} anos sua categoria é INFANTIL!'.format(age))
elif age <= 19:
    print('Você tem {} anos sua categoria é JUNIOR!'.format(age))
elif age == 20:
    print('Você tem {} anos sua categoria é SÊNIOR!'.format(age))
else:
    print('Você tem {} anos sua categoria é MASTER!'.format(age))