num = int(input('Digite um número e lhe diremos quanto vale seu fatorial: '))
origin_num = num
fatorial = 1
while num != 1:
    fatorial = fatorial * num
    num = num - 1
print('{}! = {}'.format(origin_num, fatorial))
