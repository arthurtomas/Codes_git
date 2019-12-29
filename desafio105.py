def boletim(*num):
    info = {'Total': len(*num), 'Maior': max(*num), 'Menor': min(*num), 'Média': sum(*num) / len(*num)}
    if info["Média"] < 5:
        info['Situação'] = 'Ruim'
    elif info["Média"] < 7:
        info['Situação'] = 'Razoável'
    else:
        info['Situação'] = 'Boa'
    return info


def receb_notas():
    notas = []
    nota = 0
    while nota != 99:
        nota = float(input('(Digite 99 para sair) Nota: '))
        if nota == 99:
            break
        elif 0 <= nota <= 10:
            notas.append(nota)
        else:
            print('Digite uma opção válida!')
    return notas


def situ():
    situ = str(input('Deseja saber a situação? [S/N]: '))
    return situ


a = receb_notas()
situ = situ()
if situ in 'Ss':
    print(boletim(a))
elif situ in 'Nn':
    info = boletim(a)
    del info["Situação"]
    print(info)

