
def test(s):
    A = 0
    a = 0
    for c in s:
        if c.isupper():
            A += 1
        elif c.islower():
            a += 1
    print("The number of upper case letters: ", A)
    print("The number of lower case letters: ", a)

s = str(input())
test(s)
