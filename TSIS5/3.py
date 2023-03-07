
import re

txt = str(input())

x = re.search('^[a-z]+_[a-z]+$', txt)

print(x)
