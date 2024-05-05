import re

cpf = "123.640.879-96"
cpf_reg_exp = re.compile(r"^\d{3}\.\d{3}\.\d{3}-\d{2}$")
print(cpf_reg_exp.search(cpf))
