# 1.Calcule a média das pontuações de cada equipe e armazene esses valores em uma nova lista chamada medias.

pontos = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
equipes = ['Time 1', 'Time 2', 'Time 3', 'Time 4', 'Time 5', 'Time 6', 'Time 7', 'Time 8', 'Time 9', 'Time 10', 'Time 11']
medias = []

for i in range(len(equipes)):
    pontos_time = pontos[i::len(equipes)]
    media = sum(pontos_time) / len(pontos_time)
    medias.append(media)

print(medias)

