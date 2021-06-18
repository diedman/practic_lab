import re

def mail_check(mail):
    pattern=r"^\w+[@][a-z]{2,6}(\.[a-z]{2,4}){1,2}$"
    number_re=re.compile(pattern)
    return bool(number_re.findall(mail))
