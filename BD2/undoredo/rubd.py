import json

with open("/home/aluno/Imagens/undoredo/metadado.json") as dadosini:    #le todo o arquivo em "dadosini"
    dicionario = json.load(dadosini)    #salva os dados em um formato manipulavel
    print(dicionario["INITIAL"])
    a1=dicionario["INITIAL"]["A"][0]    #salva um dado especifico em uma variavel
    print(a1)
