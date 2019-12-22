# Lista usada
boletim = []

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

# Impressão das notas individuais
estudante = -1
while estudante != 999:
    estudante = int(input('Mostrar notas de qual aluno? (Digite 999 para sair): '))
    if estudante != 999:
        print(f'Notas de {boletim[estudante][0]}: {boletim[estudante][1]}')
        print('-=' * 30)
