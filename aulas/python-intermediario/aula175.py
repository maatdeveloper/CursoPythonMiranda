from itertools import groupby


def ordena(aluno):
    return aluno["nota"]


#Aula sobre groupby
alunos1 = [
    {"nome": "Matheus", "nota": "S"},
    {"nome": "Julio", "nota": "A"},
    {"nome": "Tiago", "nota": "B"},
    {"nome": "Sergio", "nota": "B"},
    {"nome": "Jonathan", "nota": "C"},
    {"nome": "Silvio", "nota": "A"},
    {"nome": "Joao", "nota": "B"},
    {"nome": "Eduardo", "nota": "A"},
    {"nome": "Bruno", "nota": "C"}
]
alunos_agrupados = sorted(alunos1, key=ordena)
grupo1 = groupby(alunos_agrupados, key=ordena)

for chave, grupo in grupo1:
    print(chave)
    for aluno in grupo:
        print(aluno["nome"])


print()
alunos2 = ['a','a','a','b','c']
grupo2 = groupby(sorted(alunos2))

for chave, grupo in grupo2:
    print(chave)
    print(list(grupo))
