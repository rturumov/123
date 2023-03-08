
from time import sleep
import math

def square(number, s):
    sleep(s / 1000)
    return math.sqrt(number)

x = int(input())
y = int(input())

print("Square root of", x, "after", y, "miliseconds is", square(x, y))
