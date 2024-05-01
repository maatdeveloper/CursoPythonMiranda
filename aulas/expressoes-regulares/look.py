import re
from pprint import pprint

texto = """
ONLINE 192.168.0.1 GHIJK active
OFFLINE 192.168.0.2 GHIJK inative
OFFLINE 192.168.0.3 GHIJK active
ONLINE 192.168.0.4 GHIJK active
ONLINE 192.168.0.5 GHIJK inative
OFFLINE 192.168.0.6 GHIJK active
"""

#Positive lookahead
pprint(re.findall(r"\w+\s+(\d+.\d+.\d+.\d+) \w+\s+(?=active)", texto))
#Negative lookahead
pprint(re.findall(r"\w+\s+(\d+.\d+.\d+.\d+) \w+\s+(?=inative)", texto))

#Positive lookbehind
pprint(re.findall(r"(?<=ONLINE)\s+(\d+.\d+.\d+.\d+) \s+\w+\s+\w+", texto))
#Negative lookbehind
pprint(re.findall(r"(?<!ONLINE)\s+(\d+.\d+.\d+.\d+) \s+\w+\s+\w+", texto))