#try, except, else e finally
try:
    a = 10
    b = 0
    print("Ira imprimir")
    c = a / b
    print("Nao ira imprimir")
except ZeroDivisionError:
    print("Nada pode ser dividido por zero")
except NameError:
    print("Variavel nao definida")
finally:
    print("Independente do erro, estou aqui")
    
#Podemos lançar erros
print(123)
raise ValueError("Nao pode")