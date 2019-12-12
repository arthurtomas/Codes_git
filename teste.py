total = 0
n = int(input('Digite um número:'))
for c in range(1, n+1):
    if n % c == 0:
        total += 1
if total == 2:
    print('O número {} é primo!'.format(n))
elif n == 1:
    print('O número {} é primo!'.format(n))
elif n == 0:
    print('O número {} NÃO é primo!'.format(n))
elif total > 2 and n == 0:
    print('O número {} NÃO é primo!'.format(n))