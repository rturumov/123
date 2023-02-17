

def histogram(x):
    for i in x:
        print("*"*i)


n = int(input())
l = list()
for i in range(n):
    x = int(input())
    l.append(x)
histogram(l)
