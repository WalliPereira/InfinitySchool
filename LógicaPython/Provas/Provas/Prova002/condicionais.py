#Crie um programa em Python para verificar se um número é positivo, negativo ou zero. O programa deve solicitar ao usuário que insira um número e, em seguida, imprimir uma mensagem indicando a natureza do número.



num = float(input("Digite um número: "))

if num > 0:
    print(f'O numero {num} é positivo.')
elif num < 0:
    print(f'O numero {num} é negativo.')
else:
    print(f'O numero {num} é zero.')
