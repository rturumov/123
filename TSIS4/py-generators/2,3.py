
def generator(n):
    for i in range(n): 
        if i % 3 == 0:
            yield i
        elif i % 4 == 0:
            yield i

n = int(input())
for x in generator(n):
    print (x)