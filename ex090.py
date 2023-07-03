#Exercício 90: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
aluno = {}
aluno['Nome'] = str(input("Digite o nome do Aluno: "))
aluno['Média'] = float(input(f"Digite a média do aluno {aluno['Nome']}: "))
if aluno['Média'] >= 7:
    aluno['Situação'] = str("Aprovado")
elif 5 <= aluno['Média'] < 7:
    aluno['Situação'] = str("de Recuperação")
else:
    aluno['Situação'] = str("Reprovado")
print('-' * 40)
print(f"O aluno {aluno['Nome']} teve a média de {aluno['Média']} e está {aluno['Situação']}")