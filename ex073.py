#Exercício 73: Crie uma tupla preenchida com os 20 primeiros colocados do campeonato brasileiro na ordem de colocação. Depois mostre:
#A - Apenas os 5 primeiros colocados:
#B - Os 4 últimos colocados
#C - Uma lista com os times em ordem alfabética
#D - Em que posição está o time Chapecoense
times = ('Botafogo', 'Palmeiras', 'Flamengo', 'Atlético-MG', 'Fluminense', 'Grêmio',
         'Athletico-PR', 'São Paulo', 'Cruzeiro', 'Internacional', 'Fortaleza',
         'Bragantino', 'Santos', 'Cuiabá', 'Bahia', 'Corinthians', 'Goiás', 'América-MG',
         'Vasco da Gama', 'Coritiba')
tuplaordem = sorted(times)

print(f"Os 5 primeiros colcoados do Campeonato Brasileiro são {times[:5]}")
print(f"Os 4 últimos colcoados do Campeonato Brasileiro são {times[-4:]}")
print (f"Em ordem alfabética: {tuplaordem}")
print(f"A Chapecoense está na série B em 2023, mas o Corinthians está na {times.index('Corinthians') + 1}ª posição.")
