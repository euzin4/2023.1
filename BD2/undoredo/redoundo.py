import json
import psycopg2

with open("/home/aluno/Imagens/undoredo/metadado.json") as dadosini:    #le todo o arquivo em "dadosini"
    dicionario = json.load(dadosini)    #salva os dados em um formato manipulavel
    print(dicionario["INITIAL"])
    a0=dicionario["INITIAL"]["A"][0]    #salva um dado especifico em uma variavel
    a1=dicionario["INITIAL"]["A"][1]
    b0=dicionario["INITIAL"]["B"][0]
    b1=dicionario["INITIAL"]["B"][1]
    #print(a0,a1)
    #print(b0,b1)

# Função para criar conexão no banco
def conecta_db():
  con = psycopg2.connect(host='localhost', 
                         database='urbd',
                         user='postgres', 
                         password='postgres')
  return con

# Função para criar tabela no banco
def criar_db(sql):
  con = conecta_db()
  cur = con.cursor()
  cur.execute(sql)
  con.commit()
  con.close()

# Dropando a tabela caso ela já exista
sql = 'DROP TABLE IF EXISTS public.deputados'
criar_db(sql)
# Criando a tabela dos deputados
sql = '''CREATE TABLE public.tabela 
      ( a int,
        b int
      )'''
criar_db(sql)
