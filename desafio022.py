nome = str(input('Digite seu nome completo: '))
print('Maiúsculas:', nome.upper())
print('Minúsculas:', nome.lower())
print('Número de letras:', len(nome.replace(' ', '')))
print(len(nome.split()[0]))