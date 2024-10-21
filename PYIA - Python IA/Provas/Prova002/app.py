# Crie um dicionário que irá armazenar informações de um contato, incluindo o nome, o telefone e o email.
# Peça ao usuário para fornecer esses dados, solicitando que ele insira o nome do contato, o número de telefone e o endereço de email.
# Após coletar todas as informações necessárias,
# exiba o conteúdo do dicionário, mostrando todas as informações do contato inserido pelo usuário.

infos = {}

infos['Nome'] = input('Digite seu nome: ') 
infos['Telefone'] = input('Digite seu telefone: ') 
infos['E-Mail'] = input('Digite seu email: ')

print(''' --- Contato Salvo --- ''')
for chave, valor in infos.items():
    print(f'{chave}: {valor}')
