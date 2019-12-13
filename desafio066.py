soma = 0
count = 0
while True:
    num = float(input('Digite um número (999 para sair): '))
    if num == 999:
        break
    else:
        soma += num
        count += 1
print(f'Você digitou {count} números e a soma entre eles é: {soma}')
