#Ex06. Faça um programa que peça para o usuário o nome de um aluno e 3 notas (utilizando o FOR), ao final mostre a média do aluno

usuario = input('Digite seu nome: ')

somaNota = 0 

for i in range(3):
    nota = float(input('Digite sua nota:'))
    somaNota += nota 
    
media = somaNota / 3
    
print(f'A media do aluno {usuario} é {media}')