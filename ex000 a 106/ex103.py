#Exercício 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
def ficha(nome='', gols=0):
    nome = str(input("Digite o nome do jogador: ")).strip()
    if nome == '':
        nome = "<desconhecido>"
    gols = int(input("Digite a quantidade de gols marcados: "))
    print(f'O jogador {nome} marcou {gols} gol(s) no campeonato.')


ficha()
