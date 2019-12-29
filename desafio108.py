# Importação do módulo moedas
from Codes import moeda

# Entrada de dados
num = float(input('Digite um número: '))
p_aum = float(input('Digite a porcentagem do aumento: '))
p_desc = float(input('Digite a porcentagem do desconto: '))

# Saída de dados
print('-=' * 30)
print(f'A metade de R$ {num:.2f} é R$ {moeda.metade(num):.2f}'.replace('.', ','))
print(f'O dobro de R$ {num:.2f} é R$ {moeda.dobro(num):.2f}'.replace('.', ','))
print(f'R$ {num:.2f} acrescido de {p_aum}% é igual a R$ {moeda.aumento(num, p_aum):.2f}'.replace('.', ','))
print(f'R$ {num:.2f} com desconto de {p_desc}% é igual a R$ {moeda.desconto(num, p_desc):.2f}'.replace('.', ','))
