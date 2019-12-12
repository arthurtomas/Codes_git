num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))
list = [num1, num2, num3]
list.sort()
print('O maior número é {} e o menor é {}'.format(list[2], list[0]))
