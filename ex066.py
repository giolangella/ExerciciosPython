#Exercício 66: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar 999, que é a condição de parada. No final mostre quantos núimeros foram digitados e qual foi a soma entre eles.
soma = 0
contador = 0
while True:
    n = int(input("Digite outro número inteiro (999 para cancelar): "))
    if n == 999:
        break
    soma += n
    contador += 1
print("-----Programa encerrado!-----")
print("Você digitou {} números e a soma entre eles foi de {}.".format(contador, soma))