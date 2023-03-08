
def palindrom(word):
    temp = 0
    for i in range(len(word)):
        if word[i] == word[len(word) - 1 - i]:
            temp += 1
        else:
            return False
    if temp == len(word):
        return True

x = str(input())
a = list(x)
print(palindrom(a))