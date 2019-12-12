termo = int(input('Digite o primeiro termo da P.A.:  '))
razao = int(input('Digite a razão da P.A.: '))
qnt_termos = int(input('Digite a quantidade de termos que você deseja ver: '))
c = 0
while c != qnt_termos:
    termo = termo + razao
    print('{:3}° Termo = {} '.format(c + 1, termo-razao))
    c = c + 1
