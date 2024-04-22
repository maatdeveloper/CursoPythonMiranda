class Fabricante:
    def __init__(self, nome):
        self.nome = nome
        self._carros = []
        
    @property
    def carros(self):
        return self._carros
    
    @carros.setter
    def carros(self, carro):
        self._carros.append(carro)
        
    def listar(self):
        print(f"\nTodos os carros da montadora {self.nome}")
        for car in self._carros:
            print(car.nome)
        

class Motor:
    def __init__(self, nome):
        self.nome = nome
        self._carros = []
        
    @property
    def carros(self):
        return self._carros
    
    @carros.setter
    def carros(self, carro):
        self._carros.append(carro)
        
    def listar(self):
        print(f"\nLista de carros com o motor {self.nome}")
        for car in self._carros:
            print(car.nome)
        

class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None
        
    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, motor):
        self._motor = motor
        
    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, fabricante):
        self._fabricante = fabricante
        
    def modelo(self):
        print()
        print(f"O carro {self.nome} vem da montadora {self._fabricante.nome} e tem um motor {self._motor.nome}")
        

montadora = Fabricante("GM")
print(montadora.nome)

motor = Motor("250-4.1 6c 132cv")
print(motor.nome)

carro1 = Carro("Opala SS")
carro2 = Carro("Lancer")
carro3 = Carro("Fastback")
carro4 = Carro("Civic G10")
carro5 = Carro("Dodge Challenger")
carro6 = Carro("Hilux")

montadora.carros = carro1
montadora.carros = carro5
montadora.listar()

motor.carros = carro1
motor.carros = carro2
motor.carros = carro3
motor.carros = carro4
motor.carros = carro5
motor.carros = carro6
motor.listar()

carro1.motor = motor
carro1.fabricante = montadora
carro1.modelo()