def insert_block(storage, data):
    shape_shape = {"A": [[1], [1], [1], [1]], "B": [[1, 2, 3]], "C": [[1, 2], [1, 2]], "D": [[3], [1, 2, 3]], "E": [[2], [1, 2], [1, 2]]}
    cata, height = data
    lowestpoint = 0
    lowpoint = 0
    shape_depth = 0

    shape = shape_shape.get(cata)

    for i in shape:
        shape_depth = max(len(i), shape_depth)

    for j in range(len(shape)):
        for n in range(len(storage[height+j])):
            if storage[height+j][n] != 0:
                lowpoint = n 
                lowpoint = lowpoint + 2 - shape[j][0]

            lowestpoint = max(lowpoint, lowestpoint)

    if lowestpoint + shape_depth > c:
        return storage, 1

    n = 0
    for i in shape:
        for j in range(len(i)):
            storage[height+n][lowestpoint+i[j]-1] = -1

        n += 1

    return storage, 0
    
            
global r, c

r, c, n = [int(x) for x in input().split()]

data = []
storage = []
row = []

for i in range(r):
    for j in range(c):
        row.append(0)

    storage.append(row)
    row = []


leftover = 0
space = 0


for _ in range(n):
    cata, height = [x for x in input().split()]
    data.append([cata, int(height)])

for i in data:
    storage, left = insert_block(storage, i)
    
    print(i)
    for j in storage:
        print(j) 
    print("\n")

    leftover += left

for i in storage:
    for j in i:
        if j == 0:
            space += 1

print(space, leftover)