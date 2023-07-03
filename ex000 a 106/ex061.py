#Exercício 61: Refaça o desafio 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da PA usando a estrutura while.
pt = int(input("Digite o primeiro termo da PA: "))
rz = int(input("Digite a razão da PA: "))
contador = 0
termo_atual = pt
print("Os 10 primeiros termos da PA são:")
while contador < 10:
    print(termo_atual, end= ' ')
    termo_atual += rz
    contador += 1
print("Fim!")
