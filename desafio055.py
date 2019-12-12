#Maior e menor peso da lista
list_peso = []
for c in range(0, 5):
    ele = float(input('Digite o peso: '))
    list_peso.append(ele)
list_peso.sort()
print('Maior peso: {} Kg\n'
      'Menor peso: {} Kg'.format(list_peso[4], list_peso[0]))
