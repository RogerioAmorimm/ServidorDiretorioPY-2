import rpyc
from const import *

class Client:
  print(f"Iniciando conexão com servidor de diretórios de  ip: {SERVERDIR} e porta: {PORTDIR}")
  
  conn = rpyc.connect(SERVERDIR, PORTDIR) # Connect to the server
  
  print(f"Fazendo busca de Pizzaria")
  
  nomeDir  =  conn.root.exposed_buscaServer('Pizzaria')
  
  print(f"Busca finalizada, resultado: ")
  print(nomeDir) # Print the result
