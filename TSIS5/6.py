
import re

txt = str(input())

x = re.sub("\s", ",", txt)
print(x)

q = re.sub("\s", ":", txt)
print(q)