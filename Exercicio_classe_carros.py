# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela


class Carro:
    
    def __init__(self):
        self.nome = None
        self.marca = None
        self._motor = None
        self._fabricante = None
    
    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, valor):
        self._motor = valor 

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor 
        
class Motor:
    def __init__(self, nome_motor, valvulas, cavalos):
        self.nome_motor = nome_motor
        self.valvula = valvulas
        self.cavalos = cavalos

class Fabricante:
    def __init__(self, nome):
        self.nome = None

car1 = Carro()
motr1 = Motor("pipiop", 12, 140)

car1.motor = motr1


# for infos in car1.motor:
#     print(infos)
print(car1.motor)
