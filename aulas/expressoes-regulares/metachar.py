#Meta caracteres: . ^ $ * + ? { } [ ] ( ) \ | 
# | OU
# . Qualquer caracter
# [] Conjunto de caracteres
import re

texto = """
Curso completo de Programação Orientada a Objetos (POO) com a linguagem Java. Aborda os principais conceitos como Classes, Objetos, instanciamento, abstração, encapsulamento, herança, polimorfismo e muito mais. Criado pelo professor Gustavo Guanabara para o Curso em Vídeo, explica todos os conceitos de POO de uma maneira simples, objetiva e divertida. Jova. Python. Pythan. JaaaaaaaaaaaaaVAAAAAAAAAAAAA. Pythn. python
"""

print(re.findall(r"J.va|Pyth[a,e,i,o,u]n", texto, flags=re.I))

## Aula QUANTIFICADORES
# * 0 ou n
# + 1 ou n
# ? 0 ou 1
# {n}
# {min, max}
# () [a-z,A-Z,0-9]

print(re.findall(r"Ja+va+|Py?tho*n", texto, flags=re.I))