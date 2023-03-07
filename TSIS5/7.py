
import re

txt = str(input())

x = re.sub("_", " ", txt)

x = x.title()

x = re.sub("\s", "", x)

print(x)