import json
from salvar_classe_json_a import Pessoa , caminho_arquivo

penis = []
with open(caminho_arquivo , 'r') as arquivo: 
    penis = json.load(arquivo)

pes1 = penis[0]
pes2 = penis[1]
pes3 = penis[2]

print(type(pes2))
