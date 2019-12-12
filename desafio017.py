from math import hypot
b = float(input('Digite a medida do Cateto Oposto: '))
c = float(input('Digite a medida do Cateto Adjacente: '))
a = hypot(b, c)
print('A Hipotenusa vale {}'.format(a))
