#Crie um programa em Python que simule um sistema de login. O programa deve permitir ao usuário três tentativas para acertar o nome de usuário e a senha corretos.
#Caso o usuário erre as credenciais, o programa deve fornecer uma mensagem informando quantas tentativas restam. 
#Se todas as três tentativas falharem, o programa deve usar um loop for para exibir uma mensagem de "Acesso bloqueado" repetida três vezes.

tentativas = 0
while tentativas < 3:
    nome = input('Digite seu nome: ')
    senha = input('Digite sua senha: ')

    if nome == 'Wallisson' and senha == '1234':
        print('Login efetuado com successo!')
        break
    else:
        print('Credenciais inválidas. Tente novamente.')
        tentativas += 1

if tentativas == 3:
    for i in range(3):
        print('Acesso bloqueado.')
