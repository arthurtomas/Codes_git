def voto(b_year):
    """
    -> Função para verificar obrigatoriedade do voto
    :param b_year: Ano de nascimento
    :return: voto
    """
    from datetime import datetime
    idade = datetime.today().year - b_year
    if idade < 16:
        return f'Com {idade} anos: Voto negado!'
    elif idade < 65:
        return f'Com {idade} anos: Voto obrigatório!'
    else:
        return f'Com {idade} anos: Voto opcional!'


nasc = int(input('Digite seu ano de nascimento: '))
print(voto(nasc))
