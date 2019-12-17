from random import randint
list = []
for c in range(0, 5):
    ele = randint(0, 10)
    list.append(ele)
print(f'Lista de números gerados: {list}')
print(f'Menor número da lista: {min(list)}')
print(f'Maior número da lista: {max(list)}')
