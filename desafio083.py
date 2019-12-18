expressao = input('Digite uma expressão: ')
getVals = list([val for val in expressao if val in '()'])
result = "".join(getVals)
abre = 0
fecha = 0
for simbol in result:
    if simbol == '(':
        abre += 1
    elif simbol == ')':
        fecha += 1
if abre == fecha:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está incorreta!')
