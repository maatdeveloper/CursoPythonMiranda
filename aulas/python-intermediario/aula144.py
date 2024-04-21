#Dir, Hasattr, Getattr
numero = 10
nome = "Matheus"

#Dir verifica todos os atributos do objeto
print(dir(numero))

#Hasattr verifica se o objeto tem um atributo em especifico
if hasattr(numero, "__init__"):
    print("__init__")
    
#Getattr atribui um metodo a um objeto
metodo = "upper"
if isinstance(nome, str):
    print(getattr(nome, metodo)())
