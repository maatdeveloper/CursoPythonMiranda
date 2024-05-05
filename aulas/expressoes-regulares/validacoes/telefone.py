import re

phone = "(42) 99954-9658"
phone_reg_exp = re.compile(r"[(][0-9]{2}[)] 9[0-9]{4}-[0-9]{4}")
print(phone_reg_exp.search(phone))
