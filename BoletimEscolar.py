# Listas usadas
boletim = []
aprovados = []
finais = []
reprovados = []

# Entrada de dados e verificação de saída
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    continuar = 'clear'
    media = (nota1 + nota2) / 2
    boletim.append([nome, [nota1, nota2], media])
    while continuar not in 'sSnN':
        continuar = str(input('Deseja continuar? [S/N]: '))
    if continuar in 'nN':
        break

# Impressão do boletim de todos os alunos
print('-=' * 30)
print('NOME DOS ALUNOS                   : MÉDIAS')
print('-=' * 30)
for aluno in boletim:
    print(f'{boletim.index(aluno):2}. {aluno[0]:30}: {aluno[2]:4.2f} ')
print('-=' * 30)

# Separação dos aprovados, reprovados e recuperação final
for aluno in boletim:
    if aluno[2] >= 7:
        aprovados.append(aluno)
    elif aluno[2] >= 4:
        finais.append(aluno)
    else:
        reprovados.append(aluno)

# Impressão dos aprovados, reprovados e finais
print(f'\033[7;32mAprovados:\033[m')
for aluno in aprovados:
    print(f'{aluno[0]:25} Notas: {aluno[1]} Média: {aluno[2]:.2f}')
print(f'\n\033[7;31mReprovados:\033[m')
for aluno in reprovados:
    print(f'{aluno[0]:25} Notas: {aluno[1]} Média: {aluno[2]:.2f}')
print(f'\n\033[7;33mFinais:\033[m')
for aluno in finais:
    print(f'{aluno[0]:25} Notas: {aluno[1]} Média: {aluno[2]:.2f}')
