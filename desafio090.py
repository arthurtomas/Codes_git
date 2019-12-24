# Dicionário usado
boletim = {}

# Entrada de dados
boletim['nome'] = str(input('Nome: '))
boletim['media'] = float(input(f'Média de {boletim["nome"]}: '))
if boletim['media'] >= 7:
    boletim['situacao'] = 'Aprovado'
else:
    boletim['situacao'] = 'Reprovado'

# Saída de dados
print(f'O aluno {boletim["nome"]} está {boletim["situacao"]} com média {boletim["media"]}')

