# Validando Textos
while True:
    resposta = input('Deseja continuar? [S/N] -> ')

    if resposta in ['S', 'N']:
        break

    print('Entrada inválida!')

# Validando Numeros
while True:
    numero = input('Digite um numero: ')

    if numero.isdigit():
        numero = int(numero)
        break

    print('Entrada inválida!')