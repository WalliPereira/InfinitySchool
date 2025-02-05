import os

def listarArquivos():
    diretorioAtual = os.getcwd()
    itens = os.listdir(diretorioAtual)

    print(f'Conteudo do diretorio: {diretorioAtual}\n')
    for item in itens:
        print(item)

if __name__ == "__main__":
    listarArquivos()