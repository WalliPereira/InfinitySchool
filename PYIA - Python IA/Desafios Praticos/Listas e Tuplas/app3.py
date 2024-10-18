# 3.Crie uma nova lista chamada classificacao que contém tuplas, onde cada tupla contém o nome da equipe e sua média de pontuações.

pontos = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
equipes = ['Time 1', 'Time 2', 'Time 3', 'Time 4', 'Time 5', 'Time 6', 'Time 7', 'Time 8', 'Time 9', 'Time 10', 'Time 11']
medias = []

for i in range(len(equipes)):
    pontos_time = pontos[i::len(equipes)]
    media = sum(pontos_time) / len(pontos_time)
    medias.append(media)

classificacao = list(zip(equipes, medias))

print("classificacao")
for i, (time, media) in enumerate(classificacao):
    print(f"{time}: {media:.2f}")