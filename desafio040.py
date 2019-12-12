n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1 + n2) / 2
if n1 > 10 or n1 < 0 or n2 > 10 or n2 < 0:
    print('Você digitou notas inválidas.')
elif media < 5:
    print('Sua média é \033[1;31m{:.1f}\033[m, você está \033[1;31mreprovado!\033[m'.format(media))
elif media >= 5 and media < 6.9:
    print('Sua média é \033[1;33m{:.1f}\033[m, você está \033[1;33mem Recuperação!\033[m'.format(media))
else:
    print('Sua média é \033[1;36m{:.1f}\033[m, Parabéns, você está \033[1;36mAprovado!\033[m'.format(media))