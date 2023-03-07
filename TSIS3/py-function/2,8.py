
def spy_game(l):
    l1 = list()
    for i in range(len(l)):
        if l[i] == 7:
            l1.append(i)
            break
        elif l[i] == 0:
            l1.append(i)
    l2 = l1
    if l2 == l1 and len(l1) >= 3:
        return True
    else:
        return False

x = list(map(int, input().split(' ')))
print(spy_game(x))