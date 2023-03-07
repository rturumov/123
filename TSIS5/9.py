
import re

txt = str(input())

x = re.findall('[A-Z][^A-Z]*', txt)

print(' '.join(x))
