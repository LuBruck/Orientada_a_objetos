from abc import ABC, abstractmethod

class Conta(ABC):

    def __init__(self, agencia, numero_da_conta, saldo = 0):
        self.agencia = agencia
        self.numero_da_conta = numero_da_conta
        self.saldo:float = saldo


    def depositar(self, deposito):
        self.saldo += deposito
        print(f"Voce depositou R${deposito}" )

    @abstractmethod
    def sacar(self):
        ...


class ContaCorrente(Conta):
    def __init__(self, agencia, numero_da_conta, saldo=0, limite_exta = 0):
        super().__init__(agencia , numero_da_conta , saldo)
        self.limite_exta : float = limite_exta

    def sacar(self, saque):
        if self.saldo-saque >= (-1 * self.limite_exta):
            self.saldo -= saque
            print(f"Voce sacou R${saque}, e possui R${self.saldo} na conta" )
            return self.saldo
        else:
            print(f"Sem saldo suficiente: R${self.saldo}")

class ContaPoupanca(Conta):

    def __init__(self, agencia, numero_da_conta, saldo=0):
        super().__init__(agencia , numero_da_conta , saldo)

    def sacar(self, saque):
        if self.saldo - saque >= 0:
            self.saldo -= saque
            print(f"Voce sacou R${saque}" )
            return self.saldo
        else:
            print(f"Sem saldo suficiente: {self.saldo}")



if __name__ == '__main__':
    c1 = ContaCorrente(10, '10.4.710' )
    c2 = ContaPoupanca(20, '40.10.4.0')

    c2.depositar(1908)
    c2.sacar(10)
    # c3 = Conta(40, '10.50.13')
    print(c2.saldo)