
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self): 
        self.x = int(input())
        self.y = int(input())

    def show(self):
        print('(',self.x,';',self.y,')')

    def dist(self):
        self.a = int(input())
        self.b = int(input())
        k = (((self.x - self.a) ** 2) + ((self.y - self.b) ** 2))
        print (k ** (0.5))
x = int(input())
y = int(input())
a = Point(x, y)
a.show()
a.move()
a.show()
a.dist()






