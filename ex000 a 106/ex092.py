#Exercício 92: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import date
trabalhador = {}
trabalhador["Nome"] = str(input("Digite o nome: "))
nasc = int(input("Digite o ano de nascimento: "))
trabalhador["Idade"] = date.today().year - nasc
trabalhador['CTPS'] = int(input("Digite o número da CTPS ou 0 se não tem: "))
if trabalhador['CTPS'] != 0:
    trabalhador['Primeiro Emprego'] = int(input("Digite o ano do primeiro emprego: "))
    trabalhador['Salário'] = float(input("Digite o valor do salário: R$"))
    trabalhador['Idade Aposentadoria'] = trabalhador["Idade"] + ((trabalhador['Primeiro Emprego'] + 35) - date.today().year)
print("-" * 40)
print("== RELATÓRIO DE TRABALHADOR ==")
print("-" * 40)
for k, v in trabalhador.items():
    print(f"{k}: {v}")