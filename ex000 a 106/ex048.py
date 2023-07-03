#Exercício 48: Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de 3 e que se encontram no intervalo de 1 até 500.
s = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
print("A soma de todos os números ÍMPARES múltiplos de 3 entre 1 e 500 é de {}".format(s))
