#Analisador de Palíndromos
import unidecode
frase0 = str(input('Digite uma frase para verificarmos se ela é um palíndromo: '))
frase1 = frase0.replace(' ', '').lower()
reverse = frase1[::-1]
unaccented_frase1 = unidecode.unidecode(frase1)
unaccented_revese = unidecode.unidecode(reverse)
if unaccented_revese == unaccented_frase1:
    print('A frase abaixo é um palíndromo:\n\033[1;30m{}\033[m'.format(frase0))
else:
    print('A frase abaixo não é um palíndromo:\n\033[1;30m{}\033[m'.format(frase0))
