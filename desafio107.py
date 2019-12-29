# Importação do módulo moedas
from Codes import moeda

# Entrada de dados
num = float(input('Digite um número: '))
p_aum = float(input('Digite a porcentagem do aumento: '))
p_desc = float(input('Digite a porcentagem do desconto: '))

# Saída de dados
print('-=' * 30)
print(f'A metade de {num} é {moeda.metade(num)}')
print(f'O dobro de {num} é {moeda.dobro(num)}')
print(f'{num} acrescido de {p_aum}% é igual a {moeda.aumento(num, p_aum)}')
print(f'{num} com desconto de {p_desc} é igual a {moeda.desconto(num, p_desc)}')
