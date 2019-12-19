# Listas e Variáveis
people = []
information = []
leave = 'clear'
pesado = 0
leve = 999
person_pesado = person_leve =[]
p_pesadas = []
p_leves = []

# Entrada de dados
while True:
    information.append(str(input('Nome: ')))
    information.append(int(input('Peso: ')))
    print('-=' * 30)
    people.append(information[:])
    information.clear()
    leave = 'clear'
    while leave not in 'nNsS':
        leave = str(input('Deseja sair? [S/N]: '))
    if leave in 'sS':
        break

# Verificação de mais pesado e mais leve
for person in people:
    if person[1] > pesado:
        person_pesado = person
        pesado = person[1]
    if person[1] < leve:
        person_leve = person
        leve = person[1]

# Saída de dados
print('-=' * 30)
print(f'Foras cadastradas {len(people)} pessoas.')
for p in people:
    if p[1] == pesado:
        p_pesadas.append(p[0])
print(f'O maior peso foi {pesado} Kg. Pessoas com esse peso: {p_pesadas}')
for p in people:
    if p[1] == leve:
        p_leves.append(p[0])
print(f'O menor peso foi {leve} Kg. Pessoas com esse peso: {p_leves}')
print('-=' * 30)
