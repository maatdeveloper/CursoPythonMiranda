import re

email = "exemple@gamil.com"
email_reg_exp = re.compile(r"^\w+(?:[.\-\+\!\%]\w+)*@\w+(?:[.\-]\w+)*")
print(email_reg_exp.search(email))
