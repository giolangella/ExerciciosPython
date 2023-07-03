"""Exercício 44: Elabore um programa que calcule o valor de um produto, considerando sua forma de pagamento:
A vista DINHEIRO/CHEQUE - 10% de desconto
A vista no cartão - 5% de desconto
Em até 2x no cartão - preço normal
Em 3x ou mais no cartão - 20% de juros"""
valor = float(input("Digite o valor do produto: R$"))
formapgto = int(input('''Escolha a forma de pagamento:

[1] Dinheiro/Cheque à vista
[2] Cartão Débito/Crédito à vista
[3] Cartão Parcelado

Qual opção desejada? '''))
if formapgto == 1:
    valorfinal = valor - (valor * 0.1)
    print ("O valor do produto para pagamento à vista no dinheiro ou cheque com 10% de desconto será de R${:.2f}".format(valorfinal))
elif formapgto == 2:
    valorfinal = valor - (valor * 0.05)
    print ("O valor do produto com 5% de desconto para pagamento à vista no cartão será de R${:.2f}".format(valorfinal))
elif formapgto == 3:
    parcelas = int(input("Digite o número de parcelas que deseja: "))
    if parcelas == 2:
        print("O valor do produto parcelado em 2x sem juros no cartão é de R${:.2f}.".format(valor))
    elif parcelas >= 3:
        valorfinal = valor + (valor * 0.2)
        print("O valor do produto parcelado em {}x com 20% de juros é de R${:.2f}".format(parcelas, valorfinal))
    else:
        print ("Número de parcelas inválido! Transação CANCELADA!")
else:
    print("Forma de pagamento inválida! Transação CANCELADA!")