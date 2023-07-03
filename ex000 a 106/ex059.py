#Exercício 59: Crie um programa que leia dois valores e mostre um menu na tela:
#[1] Somar
#[2] Multiplicar
#[3] Maior
#[4] Novos Números
#[5] Sair do Programa
#Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
opcao = 0
while opcao != 5:
    print("""-----MENU-----"
[1] Somar"
[2] Multiplicar"
[3] Maior"
[4] Novos Números
[5] Sair do Programa""")
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        soma = n1 + n2
        print("A soma entre {} e {} é {}.".format(n1, n2, soma))
    elif opcao == 2:
        mult = n1 * n2
        print("A multiplicação entre {} e {} é {}.".format(n1, n2, mult))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print("O maior número entre {} e {} é {}".format(n1, n2, maior))
    elif opcao == 4:
        print("Informe novos números")
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
    elif opcao == 5:
        print("Finalizando...")
    else:
        print("Opção inválida! Tente novamente")
    print('=-=' * 10)
    sleep(1.5)
print("Programa encerrado! Volte sempre!")
