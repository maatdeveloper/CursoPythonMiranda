def criar_funcao(func):
    def interna(*args, **kwargs):
        print("Vou te decorar")
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)
        print(f"O seu resultado foi {resultado}")
        print("Voce foi decorado otario")
        return resultado
    return interna


@criar_funcao
def inverte_string(string):
    return string[::-1]


def e_string(param):
    if isinstance(param, str):
        return param
    else:
        raise TypeError("param deve ser uma string")


invertida = inverte_string("123")
print(invertida)
