import json

class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

caminho_arquivo = 'salvar_classe.json'
pessoa1 = Pessoa('jonas', 15)
pessoa2 = Pessoa('Robson', 409)
pessoa3 = Pessoa('Creuza', 79)

p = [pessoa1, pessoa2, pessoa3]

for nun in range(len(p)):
    p[nun] = vars(p[nun])

with open(caminho_arquivo , 'w') as arquivo:
    json.dump(p, arquivo)

