
import re

txt = str(input())

x = re.search('^[A-Z]+([a-z]+)+$', txt)

print(x)