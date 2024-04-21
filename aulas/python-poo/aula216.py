#Agregação
class CarrinhoDeCompras:
    def __init__(self):
        self._produtos = []
        
    def inserir_produtos(self, *produtos):
        for prod in produtos:
            self._produtos.append(prod)
        
    def total(self):
        return f"R$ {sum([prod.preco for prod in self._produtos]):.2f}"
        
    def listas_produtos(self):
        for prod in self._produtos:
            print(f"{prod.nome} : R$ {prod.preco:.2f}")

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        
carrinho = CarrinhoDeCompras()
p1 = Produto("Caneca", 15.69)
p2 = Produto("Camisa preta", 29.99)
p3 = Produto("Livro Python", 69.59)

carrinho.inserir_produtos(p1, p2, p3)
carrinho.listas_produtos()
print(carrinho.total())
