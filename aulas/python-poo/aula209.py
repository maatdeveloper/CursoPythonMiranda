class Pessoa:
    ano = 2024
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    #Recebe a instancia como parametro
    def metodo_normal(self):
        print(f"Oi {self.nome}")
        
    
    @classmethod #Recebe como parametro a propria classe
    def metodo_de_clasee(cls, nome):
        return cls(nome, 20)
    
    
    @staticmethod #Nao tem acesso a instacia nem a propria classe
    def nunca_usado_pelo_miranda():
        print("Oi")


pessoa1 = Pessoa("Matheus", 19)
pessoa2 = Pessoa.metodo_de_clasee("Julio")
Pessoa.nunca_usado_pelo_miranda()
