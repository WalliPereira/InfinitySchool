# Ex02. Faça um programa que peça o nome e 3 notas de um aluno, ao final mostre o nome e sua média.

notas = []
notas.append(float(input('Digite a primeira nota')))
notas.append(float(input('Digite a segunda nota')))
notas.append(float(input('Digite a terceira nota')))

soma = sum(notas)

quantidadeNotas = len(notas)

result = soma / quantidadeNotas

print (f'Sua media é : {round(result, 1)}')