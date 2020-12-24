import rpyc
import socket
from const import * #-
from rpyc.utils.server import ForkingServer
 
class Pizzaria(rpyc.Service):
  value = []

  def exposed_append(self, data):
    
    print(f"Concatenando valor: {data}")
    self.value = self.value + [data]
    return self.value

  def exposed_value(self):
    print(f"Retornando valor")
    return self.value
  
  def exposed_remove(self, data):
    if data in self.value:
      print(f"Removendo valor")
      self.value.remove(data)
      return self.value

  def exposed_search(self, data):
    if data in self.value:
      print(f"Retornando valor e posicao")
      return (data, self.value.index(data) + 1) 
           
if __name__ == "__main__":
  print(f"Criaando server Pizzaria") 
  server = ForkingServer(Pizzaria, port = PORT)
  print(f"Conectando ao Server de diretório")  
  conn_serverDir = rpyc.connect(SERVERDIR,PORTDIR)
  print(f"Obtendo ipadress da Pizzaria")  
  ipAdress = socket.gethostbyname(socket.gethostname())
  print(f"Registrando no Server de diretório") 
  conn_serverDir.root.exposed_registraServer('Pizzaria',ipAdress,PORT)
  server.start()

