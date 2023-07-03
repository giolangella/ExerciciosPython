#Exercício 31: Desenvolva um programa que pergunte a distância de uma viagem em KM. Calcule o preço da passagem cobrando R$0,50 por KM para viagens até 200km e R$0,45 para viagens mais longas.
km = float(input("Digite a distância do seu destino em km: "))
print ("Você está prestes a começar uma viagem de {}km.".format(km))
if km <= 200:
    preco = km * 0.50
else:
    preco = km * 0.45
print('O valor da sua passagem é R${:.2f}'.format(preco))