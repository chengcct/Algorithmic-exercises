import re

s = 'cheng.cct@outlook.com'
try:
    x = re.match(r'^[a-zA-Z0-9-_.]+@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*\.[a-zA-Z0-9]{2,6}$', s)
    print(x.group())
except:
    print('error')
