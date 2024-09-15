inicio = int(input('Digite o inicio da contagem: '))
final = int(input('Digite o final da contagem: '))

contador = inicio
incremento = +1 if inicio < final else -1

while contador != (final + incremento):
    print(contador)
    contador += incremento
    
print('Fim da contagem!')