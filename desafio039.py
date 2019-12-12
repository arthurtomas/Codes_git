birth = int(input('Digite seu ano de nascimento: '))
age = 2019 - birth
if age == 18:
    print('Você está na idade de Alistamento militar!')
elif age < 18:
    print('Você ainda não está na idade de Alistamento Militar.\n'
          'Você estará apto ao Alistamento em {} ano(s).'.format(18 - age))
else:
    print('Você está atrasado com sua obrigação de Alistamento Militar.\n'
          'Você deveria ter se alistado {} ano(s) atrás.'.format(age - 18))
