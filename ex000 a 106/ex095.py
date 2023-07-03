#Exercício 95: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
time = []
jogador = {}
partidas = []
while True:
    jogador.clear()
    jogador["Nome"] = str(input("Digite o nome do jogador: "))
    total = int(input(f"Quantas partidas {jogador['Nome']} jogou? "))
    partidas.clear()
    for c in range(1, total + 1):
        partidas.append(int(input(f"Quantos gols foram marcados na partida {c}: ")))
    jogador["Gols"] = partidas[:]
    jogador["Total de Gols"] = sum(partidas)
    time.append(jogador.copy())
    continuar = str(input('Deseja continuar? [S/N] ')).upper().title()
    if continuar not in 'SN':
        continuar = str(input('Opção inválida! Deseja continuar? [S/N] ')).upper().title()
    if continuar == 'N':
        break
print('-' * 40)
print("Cod", end=' ')
for i in jogador.keys():
    print(f'{i:^15}', end='')
print()
print("=" * 40)
for k, v in enumerate(time):
    print(f"{k:^4} ", end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print("=" * 40)
while True:
    busca = int(input("Mostrar dados de qual jogador? (999 para cancelar) "))
    if busca == 999:
        print("Sistema encerrado!")
        break
    if busca >= len(time):
        print(f"Erro! Não existe jogador código {busca}")
    else:
        print('-' * 40)
        print(f'RELATÓRIO DO JOGADOR {time[busca]["Nome"]}: ')
        for i, v in enumerate(time[busca]["Gols"]):
            print(f'Na partida {i} fez {v} gols.')
        print(f'Marcando um total de {jogador["Total de Gols"]} gols.')
        print('-' * 40)
