import json

pessoa = {
    'nome': "Matheus Carvalho ",
    'sobrenome': "Garcia",
    'enderecos': [
        {'rua': "Prof Judith Macedo Silveira", 'numero':27}
    ],
    'altura': 1.83,
    'peso': 65,
    'dev': True
}

with open("aulas\\python-intermediario\\aula190.json", 'w') as arquivo:
    json.dump(pessoa, arquivo, indent=2)
