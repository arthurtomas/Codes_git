from useful import menu_princ, menu_opcao, cabecalho, print_linha

menu_princ()
while True:
    x = menu_opcao()
    if x == 1:
        cabecalho('1. Pessoas Cadastradas')
        f = open("pessoascadastradas.txt", "r")
        print(f.read())
        f.close()
        print_linha()
    elif x == 2:
        cabecalho('2. Cadastrar nova pessoa')
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        f = open("pessoascadastradas.txt", "a")
        f.write(f'{nome}, {idade} anos\n')
        f.close()
        print_linha()
    elif x == 3:
        cabecalho('Saindo do Sistema...')
        break
