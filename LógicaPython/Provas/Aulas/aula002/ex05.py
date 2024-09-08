#Ex05. Faça um programa que peça um numero, e informe se ele é positivo, negativo ou neutro (igual a zero).

num = int(input('Digite um numero: '))
neutro = 0

if num > neutro:
    print('Seu numero é positvo')
elif num == neutro:
    print('Seu numero é neutro')
else:
    print('Seu numero é negativo')