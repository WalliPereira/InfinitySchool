# Crie dois conjuntos, A e B, e realize a união dos dois conjuntos.

conjunto_A = set()
conjunto_B = set()

conjunto_A.add('Perto')
conjunto_B.add('Da Rua')


# Realizando a união dos conjuntos diretamente no print
print(conjunto_A.union(conjunto_B))

# Outra forma

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Realizando a união dos conjuntos
uniao = A.union(B)

print(uniao)
