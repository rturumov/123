def has_33(x):
    number = False
    for value in x:
        if number == value == 3:
            return True
        number = value
    return False


list = list(map(int, input().split(' ')))
print(has_33(list))