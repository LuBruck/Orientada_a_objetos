from abc import ABC, abstractmethod
from Conta_classes import ContaCorrente, ContaPoupanca

class Pessoa(ABC):
    @abstractmethod
    def __init__(self, nome, idade):
        self.nome:str = nome
        self.idade:int = idade

class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self._conta: ContaCorrente or ContaPoupanca

    @property
    def conta(self):
        return self._conta

    @conta.setter
    def conta(self, item_conta:(ContaCorrente, ContaPoupanca)):
        if not isinstance(item_conta , (ContaCorrente, ContaPoupanca)):
            raise ValueError('Nao e do tipo: ContaCorrente ou ContaPoupanca')
        self._conta = item_conta

if __name__ == '__main__':
    p1 = Pessoa('Joao', 18)
    c1 = Conta_classes.ContaCorrente(10, '10.4.90')
    cl1 = Cliente("Adilson", 20)

