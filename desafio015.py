km = float(input('Quantos Km você rodou com o carro: '))
d = int(input('Quantos dias você passou com o carro: '))
preco = (60 * d) + (0.15 * km)
print('O valor a ser pago é: R$ {:.2f}'.format(preco))
