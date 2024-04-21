#Associação
class Escritor:
    def __init__(self, nome):
        self.nome = nome
        self._ferramenta = None
        
    @property
    def get_ferramenta(self):
        return self._ferramenta
    
    @get_ferramenta.setter
    def set_ferramenta(self, ferr):
        self._ferramenta = ferr
        

class Ferramenta:
    def __init__(self, nome):
        self.nome = nome
        
    def escrever(self):
        return f"{self.nome} esta escrevendo..."
    

escritor = Escritor("Matheus")
ferramenta = Ferramenta("Caneta preta")
escritor.set_ferramenta = ferramenta
print(ferramenta.escrever())
print(escritor.set_ferramenta.escrever())
