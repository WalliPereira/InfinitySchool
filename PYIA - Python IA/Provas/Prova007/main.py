import random

def lancarDados ():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    resultado = dado1 + dado2

    # Cores para colocar no resultado e deixar mais bonitinho
    cor_vermelha = "\033[91m"
    reset = "\033[0m"
     
    print(f'O resultado dos dados são: {cor_vermelha}{resultado}{reset}')

lancarDados()
