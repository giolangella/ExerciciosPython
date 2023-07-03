#Exercício 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h mostre uma mensagem dizendo que foi multado. A multa vai custar R$7,00 por cada KM acima do permitido.
vel = float(input("Digite sua velocidade atual: "))
multa = 7
if vel > 80:
    vele = vel - 80
    print("Atenção! Você ultrapassou o limite de velocidade e foi multado!")
    print("O valor da multa é R${:.2f}".format(vele * multa))
else:
    print("Você está dentro do limite de velocidade, boa viagem!")