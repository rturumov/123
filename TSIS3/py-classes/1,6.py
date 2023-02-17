
class Prime():
    def __init__(self,thelist):
        self.thelist = thelist

    def filter(self):
        for x in self.thelist:
            n = x/2 + 1
            m = int(n)
            k = 0
            for y in range(2, m):
                if x % y == 0:
                    break
                else:
                    k += 1
            if (m - 2) == k:
                print(x)

x = int(input())
y = int(input())
z = int(input())
d = int(input())
thelist = list((x, y, z, d))
a = Prime(thelist)
a.filter()