from const import *
import rpyc
from rpyc.utils.server import ThreadedServer


class ServerDir(rpyc.Service):
    
    serverNEncontrado = f"Server não encontrado ou não existente"
    serverNRegistrado = f"Servidor nao registrado"
    ListaDir = {}
    
    def __init__(self, Dicionario):
        self.ListaDir = Dicionario

    def exposed_registraServer(self, serverName, ipAdress, portNum):
        self.ListaDir.update({serverName : (ipAdress, portNum)})
        print(f"Registrando Server")
        print(self.ListaDir)

    def exposed_buscaServer(self, serverName):
        print(f"Buscando Server")

        if  serverName in self.ListaDir:
            print(f"Server encontrado")
            return self.ListaDir[serverName]
        else:
            print(f"Server não encontrado")
            return self.serverNEncontrado

    def exposed_registraServerNovamente(self, serverName, ipAdress, portNum):
        print(f"Registrando Server Novamente")
        if serverName in self.ListaDir:
            print(f"Achou item que vai ser registrado novamente")
            self.ListaDir[serverName] = (ipAdress, portNum)
            return self.ListaDir[serverName]
        else:
            print(f"Item nao registrado")
            return self.serverNRegistrado

    def exposed_removaServer(self, serverName):
        print(f"Removendo Server")
        if  serverName in self.ListaDir:
            print(f"Achamos o server a ser removido")
            ElementoRemovido = self.ListaDir[serverName]
            print(f"Guardando o elemento: {ElementoRemovido} para ser usado no return")
            self.ListaDir.pop(key=serverName)
            print(f"Removendo elemento do servidor")
            return ElementoRemovido
        else:
            print(f"Nao achamos o server a ser removido")
            return self.serverNRegistrado

if __name__ == "__main__":
    ListaDir = {}
    print(f"Iniciando servidor de diretórios na porta: {PORTDIR}")
    serverDir = ThreadedServer(ServerDir(ListaDir), port=12307)
    serverDir.start()
