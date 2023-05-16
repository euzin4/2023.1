import json

with open("/home/aluno/Imagens/redoundo/metadado.json") as dadosi:
    data = json.load(dadosi)
    print(data["INITIAL"])
