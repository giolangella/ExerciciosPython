#Exercício 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
from datetime import date
def voto():
    from datetime import date
    ano = int(input("Digite seu ano de nascimento: "))
    idade = date.today().year - ano
    if idade < 16:
        return print(f"Sua idade é {idade}anos. Você ainda não tem idade para votar.")
    if idade >= 16 or idade < 18 or idade >= 65:
        return print(f"Sua idade é {idade}anos. Seu voto é opcional.")
    else:
        return print(f"Sua idade é {idade} anos. Seu voto é obrigatório.")



voto()
