#Exercício 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre eles, qual foi o maior e o menor. O programa deve perguntar  se o usupario quer continuar utilizando o programa.
media = 0
maior = 0
soma = 0
contador = 0

n = int(input("Digite um número inteiro: "))
menor = n
soma += n
contador += 1

continuar = str(input("Deseja continuar? [S/N] ")).strip().upper()
while continuar != 'S' and continuar != 'N':
    continuar = str(input("Opção inválida! Deseja continuar? [S/N] ")).strip().upper()
    while continuar == 'S':
        n = int(input("Digite outro número: "))
        soma += n
        contador +=1
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
        continuar = str(input("Deseja continuar? [S/N] ")).strip().upper()

media = soma / contador
print("Você digitou {} números. A média entre eles é {:.2f}. O maior número digitado foi {} e menor foi {}".format(contador, media, maior, menor))
