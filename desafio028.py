from random import randrange
pcnumber = randrange(1, 6)
usernumber = int(input('Qual número entre 1 e 5 você acha que escolhi? '))
if pcnumber == usernumber:
    print('Parabéns, você acertou!')
else:
    print('Infelizmente você errou. Eu pensei em {}.\nTalvez na próxima!'.format(pcnumber))
