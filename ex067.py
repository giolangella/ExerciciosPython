#Exercício 67: Faça um programa que mostre a tabuada de vários números, uma de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
while True:
    n = int(input("Digite o número que desejá saber a tabuada: "))
    if n < 0:
        print("Programa finalizado!")
        break
    for c in range(1,11):
        print("{} x {} = {}".format(n, c, (n * c)))
    print('-' * 30)
