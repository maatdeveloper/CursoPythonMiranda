#Usando isinstance() para verificar tipos
lista = [
    "athletico", 1, 2, {"libertadores": True}, False, [1,2,3], 1.12
]

for tipo in lista:
    print(tipo, isinstance(tipo, list))
    if isinstance(tipo, (int, float)):
        print("peroca\n")