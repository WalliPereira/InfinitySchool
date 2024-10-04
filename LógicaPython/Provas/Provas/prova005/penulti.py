num_alunos = int(input("Digite o número de alunos: "))

soma_geral = 0

for _ in range(num_alunos):
    nome = input("Digite o nome do aluno: ")
    notas = [float(input(f"Digite a nota {i+1} de {nome}: ")) for i in range(3)]
    media = sum(notas) / 3
    soma_geral += media
    status = "Aprovado" if media >= 7.0 else "Reprovado"
    
    print(f"\nAluno: {nome}\nNotas: {notas}\nMédia: {media:.2f}\nStatus: {status}")

media_geral = soma_geral / num_alunos if num_alunos > 0 else 0
print(f"\nMédia geral da turma: {media_geral:.2f}")