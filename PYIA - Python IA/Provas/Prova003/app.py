# Crie um dicionário para armazenar o nome e o preço de cinco produtos. Peça ao usuário para inserir o nome de cada produto e o respectivo preço. 
# À medida que o usuário fornece os dados, armazene cada produto como uma chave no dicionário e o preço como o valor associado a essa chave. 
# Após a inserção de todos os produtos e preços, calcule o valor total da compra somando todos os preços armazenados no dicionário. 
# Por fim, exiba o valor total da compra.

produtos = {}

for _ in range(5):
    nome = input("Digite o nome do produto: ")
    while True:
        try:
            preco = float(input(f"Digite o preço de {nome}: "))
            break
        except ValueError:
            print("Por favor, insira um número válido para o preço.")
            
    produtos[nome] = preco
valor_total = sum(produtos.values())

print(''' -----  Valor total ----- ''')
print(f"O valor total da compra é: R$ {valor_total:.2f}")
