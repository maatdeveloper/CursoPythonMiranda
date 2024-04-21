#Composição
class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []
        
    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))
        
    def listar_enderecos(self):
        print(f"Enderecos de {self.nome}")
        for endereco in self.enderecos:
            print(endereco._rua, endereco._numero)
        

class Endereco:
    def __init__(self, rua, numero):
        self._rua = rua
        self._numero = numero
        
    def __del__(self):
        print("Estou morrendo...")
        print(f"Apagando {self._rua} e {self._numero}")


cliente1 = Cliente("Matheus")
cliente1.inserir_endereco("Av Brasil", 99)
cliente1.inserir_endereco("Rua Melo Milo Mole", 24)
cliente1.listar_enderecos()

del cliente1
