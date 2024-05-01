import re
#re.A -> ASCII
#re.I -> IGNORECASE
#re.M -> MULTILNE
#re.S -> DOTALL

texto = """Meu nome é Luiz Otávio, trabalho com desenvolvimento de softwares desde 2009 usando várias linguagens, bibliotecas e frameworks diferentes.

Das linguagens de programação que trabalhei, me especializei em JavaScript, Python e PHP (tenho cursos ministrados nessas linguagens somando mais de 600 horas de conteúdo e mais de 150 mil alunos).

Também tenho vasto conhecimento em áreas relacionadas ao trabalho de desenvolvimento, como HTML, CSS, SQL e mais (soft skills).

Atuei em front-end e back-end (full stack), mobile e infraestrutura (devOps).

Também atuei no setor de provedores de internet, trabalhando com redes (wireless, fibra óptica, cabeamento, entre outras áreas) e administração de servidores Linux.

Atualmente, foco todo o meu esforço em ensinar tudo o que sei para novos desenvolvedores."""

#print(re.findall(r'[a-z0-9]+', texto, flags=re.I))
print(re.findall(r"\w+", texto))
print(re.findall(r"\w+", texto, flags=re.ASCII))
print(re.findall(r"\d+", texto))
