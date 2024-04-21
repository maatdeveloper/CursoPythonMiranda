import json

dados = {
    'nome': "Matheus",
    'idade': 19
}
with open("exercicios\\python-poo\\ex23.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados, arquivo, indent=2)
