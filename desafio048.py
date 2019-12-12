#Somador de Números Ímpares e Múltiplos de 3
s = 0
for c in range(1, 501):
    rd = c % 2 #resto da divisão inteira por dois para verificar se é par ou ímpar.
    mt = c % 3 #resto da divisão inteira por três para verificar se é múltiplo de três.
    if rd != 0 and mt == 0:
        s = s + c
print('O somatório de todos os números impáres e múltiplos de 3 de 1 até 500 é: {}'.format(s))
