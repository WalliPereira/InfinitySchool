def maior_numero(num1, num2, num3):
    print('Comparando os números inseridos...')
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print('Bem-vindo ao programa de comparação de números!')
print('Vamos descobrir qual é o maior número entre os três que você informar.')

numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
numero3 = int(input('Digite o terceiro número: '))

maior = maior_numero(numero1, numero2, numero3)

print(f'\nApós comparar, o maior número entre {numero1}, {numero2} e {numero3} é: \033[1;32m{maior}\033[0m\n')
