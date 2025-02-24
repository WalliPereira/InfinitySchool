class ContaBancaria:
    def __init__(self, titular, saldo=0.0):
        self._titular = titular
        self._saldo = saldo 
    
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor  
            print(f'Depósito de R${valor:.2f} realizado com sucesso.')
        else:
            print('O valor do depósito deve ser positivo.')
    
    def sacar(self, valor):
        if 0 < valor <= self._saldo:  
            self._saldo -= valor
            print(f'Saque de R${valor:.2f} realizado com sucesso.')
        else:
            print('Saldo insuficiente ou valor inválido.')
    
    def exibir_saldo(self):
        print(f'Saldo atual de {self._titular}: R${self._saldo:.2f}')  

if __name__ == "__main__":
    conta = ContaBancaria("Gabriel", 1000.0)
    conta.exibir_saldo()
    conta.depositar(259.0)
    conta.sacar(9.0)
    conta.exibir_saldo()
    conta.sacar(50.0)
    conta.exibir_saldo()
