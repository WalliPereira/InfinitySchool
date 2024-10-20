# Ex03. Faça um programa que peça o nome, 3 notas de um aluno, e armazene-os em um dicionário, também armazene nesse dicionário a média e a situação do aluno (>= 6 está aprovado, se não reprovado.)

dicionario = {}

dicionario['nome'] = input("Digite seu nome: ")

for i in range(1, 4):
    dicionario[f'nota{i}'] = float(input(f"Informe a nota {i}: "))
    
dicionario['media'] = (dicionario['nota1']+dicionario['nota2']+dicionario['nota3'])/3

dicionario['situacao'] = 'Aprovado' if dicionario['media'] >= 6 else 'reprovado'
print(dicionario)

