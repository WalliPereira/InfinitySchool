class Veiculo:
    def movimentar(self):
        print('Veículo está em movimento.')

class Carro(Veiculo):
    def movimentar(self):
        print('O Carro esta em movimento.')

class Moto(Veiculo):
    def movimentar(self):
        print('A moto esta acelerando.')

if __name__ == "__main__":
    veiculos = [Carro(), Moto(), Veiculo()]
    for veiculo in veiculos:
        veiculo.movimentar()