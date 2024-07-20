"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.
Conta (ABC)
    ContaCorrente
    ContaPoupanca
Pessoa (ABC)
    Cliente
        Clente -> Conta
Banco
    Banco -> Cliente
    Banco -> Conta
Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.
"""
from abc import ABC, abstractmethod

class Pessoa(ABC):

    @abstractmethod
    def __init__(self, nome, idade):
        self.nome:str = nome
        self.idade:int = idade

class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self._conta: [ContaCorrente, ContaPoupanca]

    @property
    def conta(self):
        return self._conta

    @conta.setter
    def conta(self, item_conta):
        if not isinstance(item_conta , [ContaCorrente, ContaPoupanca]):
            raise ValueError('Nao e do tipo: ContaCorrente ou ContaPoupanca')
        self.conta = item_conta

class Conta(ABC):

    def __init__(self, agencia, numero_da_conta, saldo = 0):
        self.agencia = agencia
        self.numero_da_conta = numero_da_conta
        self.saldo:float = saldo


    def depositar(self, deposito):
        self.saldo += deposito
        print(f"Voce depositou R${deposito}" )

    @abstractclassmethod
    def sacar(self):
        ...


class ContaCorrente(Conta):
    def __init__(self, agencia, numero_da_conta, saldo):
        super().__init__(agencia , numero_da_conta , saldo)
        self.limite_exta : float

    def sacar(self, saque):
        if self.saldo-saque >= (-limite_exta):
            self.saldo -= saque
            print(f"Voce sacou R${saque}, e possui R${self.saldo} na conta" )
            return self.saldo
        else:
            print(f"Sem saldo suficiente: {self.saldo}")

class ContaPoupanca(Conta):

    def __init__(self, agencia, numero_da_conta, saldo):
        super().__init__(agencia , numero_da_conta , saldo)

    def sacar(self, saque):
        if self.saldo - saque >= 0:
            self.saldo -= saque
            print(f"Voce sacou R${saque}" )
            return self.saldo
        else:
            print(f"Sem saldo suficiente: {self.saldo}")

class Banco:
    def __init__(
        self, agencias: list[int] , clientes: list[Pessoa],
        conta: list[Conta]
        ):
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.conta = conta or []

    def _checa_agencia(self, agencia):

        if agencia in self.agencias:
            print('Agencia:', True)
            return True
        else:
            print('Agencia:', False)
            return False    

    def _checa_cliente(self, cliente):
        if cliente in self.clientes:
            print('cliente:' ,True)
            return True
        else:
            print('cliente:' ,False)
            return False

    def _checa_conta(self, conta):
        if conta in self.contas:
            print('Conta:' ,True)
            return True
        else:
            print('Conta:' ,False)
            return False    

    def _checar_conta_do_cliente(self, conta:Conta, cliente:Cliente):
        if conta is cliente.conta:
            print('Conta e do cliente:' ,True)
            return True
        else:
            print('Conta e do cliente:' ,False)
            return False    

    def autenticar(self, conta:Conta, cliente:Cliente):
        return _checa_agencia(self, conta.agencia) and \
            _checa_cliente(self, cliente) and \
            _checa_conta(self , conta) and \
            _checar_conta_do_cliente(self, conta, cliente)
        
