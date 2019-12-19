# Listas e Variáveis
people = []
information = []
leave = 'clear'
pesado = 0
leve = 999
person_pesado = person_leve =[]

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
print(f'O maior peso foi de {person_pesado[0]} com {person_pesado[1]} Kg')
print(f'O menor peso foi de {person_leve[0]} com {person_leve[1]} Kg')
print('-=' * 30)
