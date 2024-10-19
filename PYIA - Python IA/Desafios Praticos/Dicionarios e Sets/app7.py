# Escreva um programa que receba duas listas e calcule a união dos elementos únicos dessas listas
# E utilize  conjuntos.

# Lista com os elementos dentros.
list1 = ['Maçã', 'Abacate', 'Morango']
list2 = ['Kiwi','Melancia','Pitanga']

# Conversão para conjuntos
conjunto_A = set(list1)
conjunto_B = set(list2)

# Calculando a união
uniao = conjunto_A | conjunto_B

print("A união dos elementos únicos das listas é", uniao)
