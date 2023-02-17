
import random

def guess(x):
    rndm = random.randint(1, 20)
    i = 0
    while i < 100:
        x = i + 1
        i = i + 1
        if x < rndm:
            print("Your guess is too low.")
            print("Take a guess.")
            x = int(input())
        elif x > rndm:
            print("Your guess is too high.")
            print("Take a guess.")
            x = int(input())
        elif x == rndm:
            txt1 = "Good job, {}! You guessed my number in {} guesses!"
            print(txt1.format(name, x))
            return 0


print("Hello! What is your name?")
name = input()
txt = "Well, {}, I am thinking of a number between 1 and 20."
print(txt.format(name))
print("Take a guess.")
num = int(input())
guess(num)
