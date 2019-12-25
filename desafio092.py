# Biblioteca importada
from datetime import datetime

# Dicionário usado
trabalhador = {}

# Entrada de dados
while True:
    trabalhador['Nome'] = str(input('Nome: '))
    trabalhador['Idade'] = datetime.now().year - (int(input('Ano de Nascimento: ')))
    trabalhador['Carteira de Trabalho'] = int(input('Carteira de Trabalho [0 se não tem]:'))
    if trabalhador['Carteira de Trabalho'] == 0:
        break
    trabalhador['Ano de Contratação'] = int(input('Ano de Contratação: '))
    trabalhador['Salário'] = int(input('Salário: R$ '))
    trabalhador['Aposentadoria'] = ((trabalhador['Idade']+trabalhador['Ano de Contratação']+35)-datetime.now().year)
    break

# Saída de dados
print('-=' * 30)
for k, v in trabalhador.items():
    print(f' -{k} tem valor {v}')
