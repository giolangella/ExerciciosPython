#Exercício 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para infeiores ou iguais, o aumento é de 15%.
sal = float(input("Digite o valor do seu salário: R$"))
if sal > 1250:
    aumento = 0.1
    nsal = sal + (sal * aumento)
    print("Seu novo salário com aumento de 10% é R${:.2f}".format(nsal))
else:
    aumento = 0.15
    nsal = sal + (sal * aumento)
    print ("Seu novo salário com aumento de 15% é R${:.2f}".format(nsal))