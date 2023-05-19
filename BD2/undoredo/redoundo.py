import json

with open("/home/aluno/Imagens/undoredo/metadado.json") as dadosini:    #le todo o arquivo em "dadosini"
    dicionario = json.load(dadosini)    #salva os dados em um formato manipulavel
    print(dicionario["INITIAL"])
    a0=dicionario["INITIAL"]["A"][0]    #salva um dado especifico em uma variavel
    a1=dicionario["INITIAL"]["A"][1]
    b0=dicionario["INITIAL"]["B"][0]
    b1=dicionario["INITIAL"]["B"][1]
    #print(a0,a1)
    #print(b0,b1)

