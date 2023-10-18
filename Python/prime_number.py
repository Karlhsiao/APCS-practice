from sys import stdin

for line in stdin:
    print(line)

    line = int(line.strip())

    for i in range(1, int((line)**-2)):
        if line % i == 0:
            print("非質數")
        
        else:
            print("質數")
