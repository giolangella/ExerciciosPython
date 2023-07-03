"""Exercício 42: Refaça o desafio 35 dos triângulos e acrescente o recurso de mostrar qual tipo de triângulo será formado:
Equilátero: todos os lados são iguais
Isósceles: dois lados iguais
Escaleno: todos os lados diferentes"""
r1 = float(input("Digite o comprimento da primeira reta: "))
r2 = float(input("Digite o comprimento da segunda reta: "))
r3 = float(input("Digite o comprimento da terceira reta: "))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print ("É possível formar um triângulo com os comprimentos informados.")
    if r1 == r2 == r3:
        print("E o triângulo será Equilátero!")
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print("E o triângulo será Isósceles!")
    else:
        print ("E o triângulo será Escaleno!")
else:
    print ("Não é possível formar um triângulo com os comprimentos informados.")
