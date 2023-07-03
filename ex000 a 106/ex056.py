#Exercício 56: Desenvolva um programa que leia o nome, idade e sexo de quatro pessoas. No final, mostre:
#A média de idade do grupo
#Qual o nome do homem mais velho
# Quantas mulheres tem menos de 20 anos.
hvelho = ""
idadehvelho = 0
soma = 0
novinhas = 0

for c in range(1, 5):
    print ("-----{}ª PESSOA-----".format(c))
    nome = str(input("Digite o nome: ")).strip().title()
    idade = int(input("Digide a idade: "))
    sexo = str(input("Digite o sexo (M/F): ")).lower().strip()
    soma += idade
    if sexo == 'm':
        if idade > idadehvelho:
            idadehvelho = idade
            hvelho = nome
    elif sexo == 'f':
        if idade < 20:
            novinhas += 1
media = soma / 4
print("A média de idade do grupo é de {:.1f} anos.".format(media))
print("O homem mais velho do grupo se chama {} e tem {} anos.".format(hvelho, idadehvelho))
print("O número de mulheres com menos de 20 anos é de {} mulheres".format(novinhas))
