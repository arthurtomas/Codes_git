nome = input('Olá, qual é o seu nome? ')
salario = float(input('Olá {}, digite seu salário atual: R$ '.format(nome)))
print('Prezado {}, seu salário com 15% de aumento passa a ser R$ {:.2f}'.format(nome, salario * 1.15))
