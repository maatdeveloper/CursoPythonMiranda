import re

string = "Este e um teste de expressoes regulares"
print(re.search(r'teste', string))
print(re.findall(r"teste", string))
print(re.sub(r"teste", "abc", string))

regex = re.compile(r"teste")
regex.search(string)
regex.findall(string)
regex.sub("abc", string)
