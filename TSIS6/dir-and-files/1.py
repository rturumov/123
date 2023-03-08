
import os

path = str(input())

print("Only directories:")
for name in os.listdir(path) :
    if os.path.isdir(name):
        print(name)


print("\nOnly files:")
for name in os.listdir(path) :
    if not os.path.isdir(name):
        print(name)

print("\nAll directories and files :")
for name in os.listdir(path):
    print(name)