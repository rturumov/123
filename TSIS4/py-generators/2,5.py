
def generator(n):
    for i in reversed(range(n)): 
        yield i

n = int(input())
for x in generator(n):
    print (x)