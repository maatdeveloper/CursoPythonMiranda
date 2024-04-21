#Introducao a programacao orientada a objetos
class Pessoa:
    athleticano = True

    def __init__(self, nome, idade, sexo):
        pass
        self.name = nome
        self.age = idade
        self.sex = sexo
    
    
    def saudacao(self):
        print(f"Prazer, eu sou {self.name} e tenho {self.age} anos")

    
p1 = Pessoa("Matheus", 19, "Masculino")
print(p1.name)
print(p1.age)
print(p1.sex)
p1.saudacao()
