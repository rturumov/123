 
def string(list):
    return ''.join(list)

def permute(a, s, e):
    if s == e:
        print(string(a))
    else:
        for i in range(s, e):
            a[s], a[i] = a[i], a[s]
            permute(a, s+1, e)
            a[s], a[i] = a[i], a[s]

x = str(input())
r = len(x)
a = list(x)
permute(a, 0, r)
 