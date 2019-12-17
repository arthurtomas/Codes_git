words = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar',
         'trabalhar', 'mercado', 'programador', 'futuro')
for element in words:
    print(f'Na palavra {element.upper()} temos as seguintes vogais: ', end='')
    for vowels in element:
        if vowels.lower() in 'aeiou':
            print(vowels, end=' ')
    print('')
