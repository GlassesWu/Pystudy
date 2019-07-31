import re

reg_string = '24593408093jfijvkdr912u90482903fjc03'

s = re.findall('\d{3}', reg_string)
print(s)

def phone_num_check(phone_num):
    s = re.findall('1',phone_num)