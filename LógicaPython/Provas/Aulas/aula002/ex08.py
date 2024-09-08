# Ex08. Faça um programa que peça a idade de uma pessoa e 
# mostre o status de obrigatóriedade de voto dela:
# - Menos que 16, não pode votar
# - Entre 16 (incluso) e 18 (excluso), voto facultativo
# - Entre 18 (incluso) e 70 (excluso), voto obrigatório
# - Maior ou igual a 70, voto facultativo

idade = int(input('Digite a sua idade: '))

if idade < 16:
    print('Você não pode votar.')
elif idade >= 18 and idade < 70:
    print('Voto obrigatório.')
else:
    print('Voto facultativo.')