import json

class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
        
    def saudacao(self):
        print(f"Prazer! Me chamo {self.nome} e tenho {self.idade}")
        

with open("exercicios\\python-poo\\ex23\\ex23.json", "r") as arquivo:
    dados = json.load(arquivo)

pia = Pessoa(nome=dados['nome'], idade=dados['idade'])
pia.saudacao()
