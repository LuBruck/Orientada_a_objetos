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

from Banco_class import Banco
from Cliente_class import Cliente
from Conta_classes import ContaCorrente, ContaPoupanca


def sacar_dinheiro(banco : Banco, conta:ContaCorrente or ContaPoupanca, 
    cliente :Cliente , valor
    ):
    if banco.autenticar(conta, cliente):
        conta.sacar(valor)

def cirar_conta(cliente : Cliente, agencia , numero_da_conta , 
                tipo_de_conta : [ContaCorrente, ContaPoupanca]):
    if not isinstance(tipo_de_conta, (ContaCorrente, ContaPoupanca)):
        raise TypeError("O tipo de conta n esta correto")
    cliente.conta = tipo_de_conta(agencia , numero_da_conta)
    

cliente1 = Cliente('Adilson', 30)
cliente1.conta = ContaCorrente(10, '10.20.50')
cliente1.conta.depositar(200)
cliente2 = Cliente('Maria', 19)
cliente2.conta = ContaCorrente(40, '10.40.20')
cliente3 = Cliente('Gabriel', 80)
cliente3.conta = ContaPoupanca(60, '90.30.77')


banco1 = Banco([10, 20 , 25], [cliente1, cliente2, cliente3], [cliente1.conta, cliente3.conta])

sacar_dinheiro(banco1, cliente1.conta, cliente1, 10)

