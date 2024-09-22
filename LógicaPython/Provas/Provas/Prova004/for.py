#Você está desenvolvendo um programa em Python para calcular a soma dos números pares dentro de um intervalo determinado pelo usuário.

inicio = int(input('Digite um numero para o inicio: '))
fim = int(input('Digite um numero para o fim: '))

soma = 0

for i in range(inicio,fim + 1):
    if i % 2 == 0:
        soma += i

if soma > 0:
    print(f'A soma dos numeros pares no intervalo de {inicio} a {fim} é: {soma}')
else:
    print('Não ha numeros pares no intervalo inferomado')