def dobro(valor, formatar=False):
    resultado = valor * 2
    if formatar:
        return moeda(resultado)
    return resultado


def metade(valor=0, formatar=False):
    resultado = valor / 2
    if formatar:
        return moeda(resultado)
    return resultado


def aumentar(valor=0, taxa=0, formatar=False):
    resultado = valor * (1 + (taxa / 100))
    if formatar:
        return moeda(resultado)
    return resultado


def diminuir(valor=0, taxa=0, formatar=False):
    resultado = valor * (1 - (taxa / 100))
    if formatar:
        return moeda(resultado)
    return resultado


def moeda(valor=0, formatar=False):
    return f'R$ {valor:.2f}'.replace('.', ',')


def resumo(valor=0, taxamais=0, taxamenos=0, formatar=False):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Valor analisado: \t{moeda(valor)}')
    print(f'Dobro do valor: \t{dobro(valor, True)}')
    print(f'Metade do valor: \t{metade(valor, True)}')
    print(f'Aumento de {taxamais}%: \t{aumentar(valor, taxamais, True)}')
    print(f'Redução de {taxamenos}%: \t{diminuir(valor, taxamenos, True)}')
    print('-' * 30)
