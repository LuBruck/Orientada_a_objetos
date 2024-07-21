import Cliente_class 
import Conta_classes

class Banco:
    def __init__(
        self, agencias: list[int] , clientes: list[Cliente_class.Cliente],
        conta: list[Conta_classes.Conta]
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
        if conta in self.conta:
            print('Conta:' ,True)
            return True
        else:
            print('Conta:' ,False)
            return False    

    def _checar_conta_do_cliente(self, conta:Conta_classes.Conta, 
        cliente:Cliente_class.Cliente
        ):
        if conta is cliente.conta:
            print('Conta e do cliente:' ,True)
            return True
        else:
            print('Conta e do cliente:' ,False)
            return False    

    def autenticar(self,
        conta:[Conta_classes.ContaCorrente, Conta_classes.ContaPoupanca], 
        cliente:Cliente_class.Pessoa
        ):
        # if not isinstance(conta, (Conta_classes.ContaPoupanca, Conta_classes.ContaCorrente)) \
        #     or not isinstance(cliente, Cliente_class.Pessoa):
            # raise ValueError("Uma das variaveis nao e do tipo certo")
        return self._checa_agencia(conta.agencia) and \
            self._checa_cliente(cliente) and \
            self._checa_conta(conta) and \
            self._checar_conta_do_cliente(conta, cliente)

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencias!r}, {self.clientes!r}, {self.contas!r})'
        return f'{class_name}{attrs}'

if __name__ == '__main__':

    cliente1= Cliente_class.Cliente('Adrey', 10)
    cliente2 = Cliente_class.Cliente('Amigo', 25)
    conta1 = Conta_classes.ContaCorrente(10, '132.14.5')
    banco1 = Banco([10,4,7], [cliente2], [conta1])
    cliente2.conta = conta1

    banco1.autenticar(conta1, cliente2)