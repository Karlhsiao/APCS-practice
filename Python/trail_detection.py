n = int(input())

data = []
facing = 1 #right 1 down 2 left 3 up 4

def move(data1, data2, facing):
    if data1[0] == data2[0]:
        if facing == 1:
            pass

for _ in range(n):
    x, y = map(int, input().split())
    data.append([x, y])

for i in range(len(data)-1):
    right, left, uturn, facing = move(data[i], data[i+1], facing)