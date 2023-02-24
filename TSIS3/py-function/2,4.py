
def filter_prime(thelist):
    for x in thelist:
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

thelist = list(map(int, input().split(' ')))
a = filter_prime(thelist)