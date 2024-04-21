cpf = '123640879'
soma = 0
regressao = 10
for d in cpf:
    cpf_int = int(d)
    soma += cpf_int * regressao
    regressao -= 1

primeiro_digito = (soma * 10) % 11
if primeiro_digito > 9:
    print('O penultimo digito de seu cpf e 0')
else:
    print(f'O penultimo digito do seu cpf e {primeiro_digito}')
