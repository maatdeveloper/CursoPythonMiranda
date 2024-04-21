#@property
class Caneta:
    def __init__(self,cor):
        self.__cor = cor
        #cor = public
        #_cor = protected
        #__cor = private
        
    @property
    def cor(self):
        return self.__cor
    
    @cor.setter
    def cor(self, cor):
        if cor == "Verde":
            raise ValueError("Nada de verde aqui")
        self.__cor = cor


caneta = Caneta("Preta")
print(caneta.cor)
caneta.cor = "Vermelho"
print(caneta.cor)
