n = input()
mirror = []
origin = 0

for _ in range(int(n)):
    temp = [int(x) for x in input().split()]
    mirror.append(temp)

print(mirror)

for i in mirror:
    if i[1] == 0:
        if i[2] == 0:
            if origin - i[1] < 0:
                

        elif i[2] == 1:

