#Exercício 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor for ímpar, desconsidere-o.
s = 0
pares = 0
for c in range(1, 7):
    n = int(input("Digite o {}º número: ".format(c)))
    if n % 2 == 0:
        s += n
        pares += 1
print("Você informou {} números pares e a soma foi de {}".format(pares, s))