#Exercício 113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
from utilidadesCeV import dados
inteiro = dados.leiaint("Digite um valor inteiro: ")
print(f"O Número inteiro digitado foi {inteiro}")
real = dados.leiafloat("Digite um valor real: ")
print(f"O Número real digitado foi {real}")