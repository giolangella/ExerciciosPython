#Exercício 96: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
def area():
    print("-" * 30)
    print("  ==CALCULO DE ÁREA==  ")
    print("-" * 30)
    l = int(input("Digite a largura em metros do terreno: "))
    c = int(input("Digite o comprimento em metros do terreno: "))
    print("-" * 30)
    area = l * c
    print(f"A área do terreno informado é de {area}m²")


area()