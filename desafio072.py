tupla_numbers = ('um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',
                 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete',
                 'dezoito', 'dezenove', 'vinte')
while True:
    print('-=' * 27)
    n = int(input('Digite um número entre 1 e 20: '))
    if n < 1 or n > 20:
        print('Número inválido, tente novamente abaixo! ')
    else:
        print(f'O número digitado foi {tupla_numbers[n-1]}.')
        break
