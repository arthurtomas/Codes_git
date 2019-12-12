import math
r = float(input('Digite um ângulo: '))
a = r * (math.pi / 180)
s = math.sin(a)
c = math.cos(a)
t = math.tan(a)
print('Para o ângulo {}° temos os seguintes valores:'.format(r))
print('Seno: {:>8.2f}\nCosseno: {:5.2f}\nTangente: {:.2f}'.format(s, c, t))
