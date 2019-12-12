n = 0
count = 0
soma = 0
print('Para sair digite o número \033[1;30m999\033[m')
while n != 999:
    n = int(input('Digite um número: '))
    soma = soma + n
    count = count + 1
print('Foram digitados {} números e a soma entre eles vale {}.'.format(count - 1, soma - 999))
