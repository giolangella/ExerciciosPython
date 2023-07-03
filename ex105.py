#Exercício 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
#A - Quantidade de notas
#B - A maior nota
#C – A menor nota
#D – A média da turma
#E – A situação (opcional)
def notas(*notas, situacao=False):
    info = {}
    info['Quantidade de notas'] = len(notas)
    info['Maior nota'] = max(notas)
    info['Menor nota'] = min(notas)
    info['Média da turma'] = sum(notas) / len(notas)

    if situacao:
        if info['Média da turma'] >= 7:
            info['Situação'] = 'BOA'
        if info['Média da turma'] >=5:
            info['Situação'] = 'MÉDIA'
        else:
            info['Situação'] = 'RUIM'

    return info


resultado_com_situacao = notas(9.5, 8.8, 7.2, 6.5, 9.0, situacao=True)
print(resultado_com_situacao)
