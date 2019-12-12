#Gerador de Progressão Aritmética
termo = int(input('Digite o primeiro termo da P.A.:  '))
razao = int(input('Digite a razão da P.A.: '))
for c in range(0, 10):
    termo = termo + razao
    print('{} '.format(termo-razao))
