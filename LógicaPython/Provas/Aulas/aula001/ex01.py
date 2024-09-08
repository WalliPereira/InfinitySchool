# Ex 2. Faça um programa que peça o dia, o mês e o ano de nascimento da pessoa utilizando o input, e mostre sua data de nascimento completa.
# Exemplo
# Entrada:
# >>> Ano de Nascimento: 2000
# >>> Mês de Nascimento: 03
# >>> Dia de Nascimento: 10

# Saida
# >>> Sua data de nascimento é 10/03/2000 

dia = input('Digite o dia de seu nascimento: ')
mes = input('Digite o mês de seu nascimento: ')
ano = input('Digite o ano de seu nascimento: ')

print(f'Sua data de nascimento é {dia}/{mes}/{ano}')
print('Sua data de nascimento é ' + dia + '/' + mes + '/' + ano)