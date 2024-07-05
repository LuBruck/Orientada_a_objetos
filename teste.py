class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def pessoa_com_50(cls, nome):
        return cls(nome, 50)

    
p1 = Pessoa("adilson", 10)
p2 = Pessoa.pessoa_com_50("jr")

print(p1.idade)
print(p2.idade)


