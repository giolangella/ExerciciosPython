"""Exercício 40: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem de acordo com a média atingida:
Média abaixo de 5 - REPROVADO
Média entre 5 e 6.9 - RECUPERAÇÃO
Média 7 ou superior - APROVADO"""
nome = str(input("Digite seu nome: ")).strip().title()
n1 = float(input("Olá {}, digite a nota da sua primeira avaliação: ".format(nome)))
n2 = float(input("Agora digite a nota da sua segunda avaliação: "))
media = (n1 + n2) / 2
if media < 5.0:
    print ("{} sua média foi de {:.2f} e você foi REPROVADO! Estude mais!".format(nome, media))
elif media >= 5.0 and media < 7:
    print ("{} sua média foi de {:.2f} e você está de RECUPERAÇÃO! Boa sorte!".format(nome, media))
else:
    print ("PARABÉNS {}!!! Sua média foi {:.2f} e você foi aprovado!".format(nome, media))