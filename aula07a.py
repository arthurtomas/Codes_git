nome = input('Digite seu nome: ')
print('Prazer em conhecê-lo {:#^20}!'.format(nome))
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1+n2)/2
print('Parabéns {} sua média foi: {:.2f}'.format(nome, m))
