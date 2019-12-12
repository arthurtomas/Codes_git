#n = float(input('Digite um número float: '))
#int = n // 1
#print('A porção inteira de {} é {:.0f}'.format(n, int))

from math import trunc
n = float(input('Digite um número float: '))
print('A parte inteira de {} é {}'.format(n, trunc(n)))

