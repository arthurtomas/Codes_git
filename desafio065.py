list_numbers = []
resp = 'S'
while resp != 'N':
    ele = int(input('Digite um número: '))
    resp = str(input('Você deseja continuar? [S/N]: ')).upper()
    list_numbers.append(ele)
media = sum(list_numbers) / len(list_numbers)
print('A média dos números digitados foi: {}'.format(media))
print('Maior número: {}'.format(max(list_numbers)))
print('Menor número: {}'.format(min(list_numbers)))
