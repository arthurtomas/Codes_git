casa = float(input('Digite o valor da casa: R$  '))
salario = float(input('Digite o seu salário: R$ '))
anos = float(input('Digite em quantos anos você pagará a casa: '))
prestacao = casa / (anos * 12)
parcmax = salario * 30/100
meses = casa / parcmax
if prestacao > parcmax:
    print('Seu empréstimo foi \033[31mnegado\033[m, porque o valor da parcela é maior que 30% do seu salário.')
    print('As parcelas ficaram no valor de \033[1;33mR$ {:.2f}\033[m'
          ', o máximo possível seria \033[1;36mR$ {:.2f}\033[m'.format(prestacao, parcmax))
    print('Com o salário de R$ {:.2f} você pagaria uma casa de R$ {:.2f} em {:.0f} '
          'meses, ou seja, aproximadamente \33[1;31m{:.1f} anos\033[m.'.format(salario, casa, meses, meses / 12))
else:
    print('Seu empréstimo foi \033[4;36maprovado!\033[m\nAs parcelas serão de '
          '\033[1;36mR$ {:.2f}\033[m'.format(prestacao))
