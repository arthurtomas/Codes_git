# Dicionário e listas usadas
person = {}
people = []
idades = []
idades_acima_media =[]
mulheres = []

# Entrada de dados
while True:
    person['Nome'] = str(input('Nome: '))
    person['Sexo'] = 'clear'
    while person['Sexo'] not in 'MmFf':
        person['Sexo'] = str(input('Sexo [M/F]: '))
        if person['Sexo'] not in 'MmFf':
            print('Erro! Digite apenas M ou F.')
    person['Idade'] = int(input('Idade: '))
    people.append(person.copy())
    person.clear()
    continuar = 'clear'
    while continuar not in 'SsNn':
        continuar = str(input('Deseja continuar? [S/N]: '))
        if continuar not in 'SsNn':
            print('Erro! Digite apenas S ou N.')
    if continuar in 'Nn':
        break

# Captação de informações adicionais

for person in people:
    idades.append(person["Idade"])
    if person["Sexo"] in 'Ff':
        mulheres.append(person["Nome"])
media_idade = sum(idades) / len(idades)
for person in people:
    if person["Idade"] > media_idade:
        idades_acima_media.append(person)

# Saída de dados
print('-=' * 30)
print(f'A) Ao todo temos {len(people)} pessoas cadastradas.')
print(f'B) A média de idade é de {media_idade:.2f} anos.')
print(f'C) As mulheres cadastradas foram {mulheres}')
print('D) Lista de pessoas que estão acima da média de idade:')
for c in idades_acima_media:
    print(f'  {c}')
print('<<ENCERADO>>')
