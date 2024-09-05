# Exibe no terminal o numero ou elemento que apareceu mais vezes.
list = [
    1,2,3,4,4,4,2,2,5,6,7,7,8,9,9,9,4,4,4,1,1,2,2,2,2,3
]

frenquente = max(set(list), key=list.count)
print(frenquente)