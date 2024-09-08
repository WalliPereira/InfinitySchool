# Ex02. Faça um programa que realize uma contagem de 10 até 1 (Regressiva)
import time

contador = 10

while contador > 0:
    print(contador)
    contador -= 1
    time.sleep(1)
    # contador = contador + 1

# \n ele quebra uma linha
print('\nFim da Contagem!')