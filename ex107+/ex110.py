#Exercício 110: Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.
import moeda
valor = float(input("Digite um valor: R$"))
taxamenos = float(input("Digite a taxa para diminuir: "))
taxamais = float(input("Digite a taxa para aumentar: "))

moeda.resumo(valor, taxamais, taxamenos)