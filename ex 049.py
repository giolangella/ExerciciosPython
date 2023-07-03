#Exercício 49: Refaça o exercício 09, mostrando a tabuada de um número que o usuário escolher, mas agora usando o laço for.
n = int(input("Digite o número que desejá saber a tabuada: "))
for c in range(1,11):
    print("{} x {} = {}".format(n, c, (n * c)))
print("FIM!")