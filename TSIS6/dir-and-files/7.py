
with open("c:/Users/User/Desktop/pp2/pp2-22B030603/TSIS6/dir-and-files/test.txt") as file:
    with open("c:/Users/User/Desktop/pp2/pp2-22B030603/TSIS6/dir-and-files/copy.txt", "w") as file1:
        for line in file:
            file1.write(line)
            