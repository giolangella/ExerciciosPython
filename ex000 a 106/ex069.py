#Exercício 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada o programa deverá perguntar se o usuário quer ou não continuar. No final mostre:
#A - Quantas pessoas tem mais de 18 anos.
#B - Quantos homens foram cadastrados.
#C - Quantas mulheres tem menos de 20 anos.
homens = 0
maiores = 0
novinhas = 0
cadastros = 0
while True:
    print("-" * 30)
    idade = int(input("Digite a idade: "))
    sexo = str(input("Digite o sexo [M/F]: ")).strip().upper()[0]
    print("-" * 30)
    while sexo not in "MmFf":
        sexo = str(input("Digite o sexo [M/F]: ")).strip().upper()[0]
    cadastros += 1
    if idade >= 18:
        maiores += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade <20:
        novinhas += 1
    print("-" * 30)
    continuar = str(input("Deseja continuar? [S/N]")).strip().upper()[0]
    print("-" * 30)
    while continuar not in "SsNn":
        print("-" * 30)
        continuar = str(input("Deseja continuar? [S/N]")).strip().upper()[0]
        print("-" * 30)
    if continuar == 'N':
        break
print(f"Foram cadastradas {cadastros} pessoas.")
print(f"{maiores} maiores de idade.")
print(f"{homens} homens.")
print(f"{novinhas} mulheres com menos de 20 anos.")
print("Programa encerrado.")

