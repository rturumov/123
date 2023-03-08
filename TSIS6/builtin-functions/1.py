
def multiply(numbers):  
    mult = 1
    for x in numbers:
        x = int(x)
        mult *= x  
    return mult  
numbers = input().split(' ')
print(multiply(numbers))