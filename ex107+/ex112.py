#Exercício 112: Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imputa(), mas com uma validação de dados para aceitar apenas valores que seja monetários.
from utilidadesCeV import moeda
from utilidadesCeV import dados
valor = dados.leiadinheiro("Digite o valor: R$")
taxamenos = dados.leiadinheiro("Digite a taxa para diminuir: ")
taxamais = dados.leiadinheiro("Digite a taxa para aumentar: ")

moeda.resumo(valor, taxamais, taxamenos)