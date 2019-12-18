# Listas que serão usadas
lista = [1, 3, 2, 7, 2, 0, 9]
lista_par = []
lista_impar = []
# Verificadores de par ou ímpar
for c in range(0, len(lista)):
    verificador_par = lista[c] % 2
    if verificador_par == 0:
        lista_par.append(lista[c])
    else:
        lista_impar.append(lista[c])
# Impressão das listas organizadas
print(f'Lista Original: {lista}')
print(f'Pares: {lista_par}')
print(f'Ímpares: {lista_impar}')
