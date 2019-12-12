#Analisador Completo
list_name = []
list_age = []
list_sex = []
oldest_man = ''
biggest_age = 0
women_under_20 = 0
for c in range(0, 4):
    print('----- {}ª PESSOA -----'.format(c+1))
    ele_name = str(input('Nome: '))
    list_name.append(ele_name)
    ele_age = int(input('Idade: '))
    list_age.append(ele_age)
    ele_sex = str(input('Sexo [M/F]: ')).upper()
    list_sex.append(ele_sex)
    if ele_sex == 'M' and biggest_age < ele_age:
        biggest_age = ele_age
        oldest_man = ele_name
    if ele_sex == 'F' and ele_age < 20:
        women_under_20 += 1
media_age = (list_age[0]+list_age[1]+list_age[2]+list_age[3]) / 4
print('A média de idade do grupo é {} anos.'.format(media_age))
print('O homem mais velho é {} com {} anos.'.format(oldest_man, biggest_age))
print('Existem {} mulheres com menos de 20 anos.'.format(women_under_20))
