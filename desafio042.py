l1 = float(input('Digite a medida de a: '))
l2 = float(input('Digite a medida de b: '))
l3 = float(input('Digite a medida de c: '))
list = [l1, l2, l3]
list.sort()
if (list[0] + list[1]) <= list[2]:
    print('É impossível formar um triângulo com essas medidas.')
else:
    print('É possível formar um triângulo com essas medidas.')
    if list[0] == list[1] == list[2]:
        print('Seu triângulo é \033[1mEquilátero!\033[m ')
    elif list[0] == list[1] != list[2] or list[0] != list[1] == list[2]:
        print('Seu triângulo é \033[1mIsósceles!\033[m ')
    else:
        print('Seu triângulo é \033[1mEscaleno!\033[m ')