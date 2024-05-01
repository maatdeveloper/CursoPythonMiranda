import re
# ^ começa com
# $ termina com

texto = "<p>Frase 1</p> <p>Eita</p> <p>Qualquer Coisa</p> <div></div>"

tags = re.findall(r"(<([pdiv]{1,3})>.+?<\/\2>)", texto)

for tag in tags:
    print(tag)
