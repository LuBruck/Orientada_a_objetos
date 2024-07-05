class Carrinho:
    def __init__(self):
        self._produtos = []

    def listar_produtos(self):
        for produto in self._produtos:
            print(produto.nome , produto.preço , "CATAPIMBA")

    def adicionar_ao_carrinho(self, *produtos):
        
        ...
