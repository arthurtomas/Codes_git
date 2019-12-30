from useful import print_linha

def recebe_peso():
    pesos = []
    for c in range(0, 7):
        peso = float(input(f'Digite o {c+1}º peso: '))
        pesos.append(peso)
    return pesos


def acima_90(lista):
    obesos = []
    for person in lista:
        if person > 90:
            obesos.append(person)
    return obesos


pesos = recebe_peso()
obesos = acima_90(pesos)
print_linha()
print(f'Quantidade de pessoas acima de 90 Kg: {len(obesos)}')
print(f'Lista de pesos acima de 90 Kg: {sorted(obesos)}')
print_linha()
print(f'A média destes pesos {sorted(pesos)} é {sum(pesos) / len(pesos):.2f} Kg')
print_linha()
