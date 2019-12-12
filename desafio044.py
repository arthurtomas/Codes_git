preco = float(input('Digite o preço do produto: R$ '))
print('\033[1;30m1. A vista.\n'
      '2. A vista no cartão.\n'
      '3. Em até 2x no cartão.\n'
      '4. A partir de 3x no cartão.\033[m')
mpagam = int(input('Digite o número correspondente ao seu modo de pagamento: '))
if mpagam == 1:
    print('O valor final do produto será: R$ {:.2f}'.format(preco-(preco*10/100)))
elif mpagam == 2:
    print('O valor final do produto será: R$ {:.2f}'.format(preco-(preco*5/100)))
elif mpagam == 3:
    print('O valor final do produto será: R$ {:.2f}'.format(preco))
elif mpagam == 4:
    print('O valor final do produto será: R$ {:.2f}'.format(preco+(preco*20/100)))
else:
    print('\033[1;31mVocê digitou uma opção inválida!\033[m ')

