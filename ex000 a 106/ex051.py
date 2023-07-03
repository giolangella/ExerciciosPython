#Exercício 51: Desenvola um programa que leia o primeiro termo e a razão de uma PA. No final mostre os 10 primeiros termos dessa progressão.
pt = int(input("Digite o primeiro termo da PA: "))
rz = int(input("Digite a razão da PA: "))

print("Os 10 primeiros termos da PA são:")
for c in range(pt, pt + 10 * rz, rz):
    print(c)