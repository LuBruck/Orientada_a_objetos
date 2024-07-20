
class Banco:
    def __init__(self):
        self._clentes = []
        self._contas_autenticacao = {
            "agencia" : ['12'], 
            "numero_e_clientes" : {
                "Nome" : ['Robson', 'Julina'],
                "numero_da_conta" : ['10.24.15', '11.24.5']
            },
        }

papa = Banco()

print(papa._contas_autenticacao['numero_e_clientes']['Nome'])



class Banco:
    def __init__(self):
        self._clentes = []
        self._contas_autenticacao = {
            "Nome" : ['Robson', 'Julina'],
            "numero_da_conta" : ['10.24.15', '11.24.5']}
        self._agencias_atuenticacao = []