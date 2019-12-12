termo = int(input('Digite o primeiro termo da P.A.:  '))
razao = int(input('Digite a razão da P.A.: '))
c = 0
while c != 10:
    termo = termo + razao
    print('{:3}° Termo = {} '.format(c + 1, termo-razao))
    c = c + 1
