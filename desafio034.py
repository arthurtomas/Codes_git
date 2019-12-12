salary = float(input('Digite seu salário atual: '))
if salary <= 1250:
    print('Seu novo salário será: R$ {:.2f}'.format(salary + (salary * 15/100)))
else:
    print('Seu novo salário será: R$ {:.2f}'.format(salary + (salary * 10/100)))
