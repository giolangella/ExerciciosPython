"""Exercício 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule o seu IMC e mostre seu status, de acordo com a tabela abaixo:
Abaixo de 18.5 - Abaixo do Peso
Entre 18.5 e 25 - Peso Ideal
25 até 30 - Sobrepeso
30 até 40 - Obesidade
Acima de 40 - Obesidade Mórbida"""
paciente = str(input("Digite o seu nome: ")).strip().title()
peso = float(input("Digite seu peso atual: "))
altura = float(input("Digite sua altura: "))
imc = peso / (altura ** 2)
if imc < 18.5:
    print("Olá {}! Seu IMC é de {:.1f} e você está ABAIXO DO PESO, considere se alimentar melhor e praticar exercícios!". format(paciente, imc))
elif imc >= 18.5 and imc <= 25:
    print("Olá {}! Seu IMC é de {:.1f} e você está no peso IDEAL! Parabéns, continue assim!".format(paciente, imc))
elif imc > 25 and imc <= 30:
    print("Olá {}! Seu IMC é de {:.1f} e você está com SOBREPESO, considere fazer uma dieta leve e praticar exercícios!".format(paciente, imc))
elif imc > 30 and imc <= 40:
    print("Olá {}! Seu IMC é de {:.1f} e você está com OBESIDADE! Considere uma dieta rigorosa com acompanhamento médico e pratique exercícios!".format(paciente, imc))
else:
    print("Olá {}! Seu IMC é de {:.1f} e você está com OBESIDADE MÓRBIDA! Procure um especialista, obesidade MATA!".format(paciente, imc))