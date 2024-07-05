class Carro():
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(self, "FEZ VRUUUUM")


celta = Carro('Celta')

celta.acelerar()