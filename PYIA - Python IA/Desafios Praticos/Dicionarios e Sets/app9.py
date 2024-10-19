# Escreva um programa que percorra as chaves e valores de um dicionário separadamente e os exiba.

dicionario = {
    'instituição': 'Infinity School',
    'Curso': 'Dev Full-Stack',
    'Módulo': 'PYIA - Python IA'
}

# Exibindo chaves e valores
print("Chaves e Valores:")
for chave in dicionario:
    print(f"{chave}: {dicionario[chave]}")