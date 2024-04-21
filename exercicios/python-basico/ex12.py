cpf = '1236408799'
soma = 0
regressao = 11

for d in cpf:
    cpf_int = int(d)
    soma += cpf_int * regressao
    regressao -= 1

ultimo_digito = (soma * 10) % 11
ultimo_digito = ultimo_digito if ultimo_digito <= 9 else 0
print(f'O ultimo digito do seu cpf e {ultimo_digito}')
