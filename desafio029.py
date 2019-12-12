speed = float(input('Digite sua velocidade: '))
if speed <= 80:
    print('Parabéns, você não foi multado.')
else:
    print('Você foi multado! O valor da sua multa é de: R$ {:.2f}'.format((speed-80)*7))
