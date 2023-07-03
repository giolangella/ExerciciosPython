#Exercício 64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar 999, que é a condição de parada. No final mostre quantos núimeros foram digitados e qual foi a soma entre eles.
n = int(input("Digite um número inteiro (999 para cancelar): "))
soma = 0
contador = 0
while n != 999:
    soma += n
    contador += 1
    n = int(input("Digite outro número inteiro (999 para cancelar): "))
print("-----Programa encerrado!-----")
print("Você digitou {} números e a soma entre eles foi de {}.".format(contador, soma))
