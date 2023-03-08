
list = input().split(' ')

with open("c:/Users/User/Desktop/pp2/pp2-22B030603/TSIS6/dir-and-files/test.txt", "w") as file:
        for c in list:
                file.write("%s\n" % c)

x = open("c:/Users/User/Desktop/pp2/pp2-22B030603/TSIS6/dir-and-files/test.txt")
print(x.read())