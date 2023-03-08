
import string
import os

for letter in string.ascii_uppercase:
    x = letter + ".txt"
    with open("c:/Users/User/Desktop/pp2/pp2-22B030603/TSIS6/dir-and-files/" + x, "w") as file:
       file.writelines(letter)