# Ex07. Faça um programa que peça 3 notas de um aluno, 
# calcule a média e mostre sua situação segundo a tabela abaixo:
# - Menor que 4, Reprovado
# - Entre 4 e 6, Recuperação
# - Maior ou igual a 6, Aprovado

nota1 = float(input('Digite a 1ª nota: '))
nota2 = float(input('Digite a 2ª nota: '))
nota3 = float(input('Digite a 3ª nota: '))

media = (nota1 + nota2 + nota3) / 3

if media < 4:
    situacao = 'Reprovado'
elif media >= 4 and media < 6:
    situacao = 'Em Recuperação'
else:
    situacao = 'Aprovado'

print(f'A média do aluno foi {media:.1f} e ele está {situacao}')