maiorNumero = None #Variavel acumuladora

while True:
    numero = int(input('Digite um numero: '))
    
    if numero > maiorNumero:
        maiorNumero = numero
        
    resposta = input('Deseja continuar? [S/N] -> ')
    
    if resposta == 'N':
        break
    
print(f'O maior numero digitado foi: {maiorNumero}')
print('Fim do Programa!')