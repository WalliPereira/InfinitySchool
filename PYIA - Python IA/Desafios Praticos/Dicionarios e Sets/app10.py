# Desenvolva um programa que recebe um dicionário uma chave e um valor como entrada.
# Adicione a chave e o valor ao dicionario
# ↑↑↑ Atualizando o valor ser a chave ja existir 

dicionario = {
    'instituição': 'Infinity School',
    'Curso': 'Dev Full-Stack',
    'Módulo': 'PYIA - Python IA'
}

chave = input('Digite a chave: ')
valor = input('Digite o valor: ')

dicionario[chave] = valor

print("\nDicionário atualizado:")
print(dicionario)