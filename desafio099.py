def maior():
    lista = []
    while True:
        num = int(input('Digite um valor(999 para sair): '))
        if num == 999:
            break
        else:
            lista.append(num)
    print('-=' * 30)
    print(f'Lista: {lista}')
    print(f'Maior número da lista: {max(lista)}')
    print(f'Quantidade de valores na lista: {len(lista)}')


maior()
