distance = float(input('Digite a distância da sua viagem: '))
if distance <= 200:
    print('Sua passagem custará R$ {:.2f}'.format(float(distance) * 0.5))
else:
    print('Sua passagem custará R$ {:.2f}'.format(float(distance) * 0.45))
