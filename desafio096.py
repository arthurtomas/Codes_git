def area(larg, comp):
    print(f'A área de um terreno {larg}m x {comp}m = {larg*comp:.2f}m²')


# Programa Principal
l = float(input('Largura(m): '))
c = float(input('Comprimento(m): '))
area(l, c)
