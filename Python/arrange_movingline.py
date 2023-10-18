def lineup(place, x1, y1, x2, y2, face):

    for i in range(x1, x2):
        for j in range(y1, y2):
            if face == 0:
                if place[i][j] == 3:
                    place[i][j] = 4
                elif place[i][j] == 0:
                    place[i][j] = 2

            elif face == 1:
                if place[i][j] == 2:
                    place[i][j] = 4
                elif place[i][j] == 0:
                    place[i][j] = 3


    return place


def removeline(place, x1, y1, x2, y2, face):

    for i in range(x1, x2):
        for j in range(y1, y2):
            if face == 0:
                if place[i][j] == 4:
                    place[i][j] = 3
                elif place[i][j] == 2:
                    place[i][j] = 0

            elif face == 1:
                if place[i][j] == 4:
                    place[i][j] = 2
                elif place[i][j] == 3:
                    place[i][j] = 0

    return place


def sticking(place, x, y):

    place[x][y] = 1

    for i in range(x+1, len(place)):

        if place[i][y] == 1:

            place = lineup(place, x+1, y, i, y+1, 0)
            break
    
    for i in reversed(range(0, x)):

        if place[i][y] == 1:

            place = lineup(place, i+1, y, x, y+1, 0)
            break

    for i in range(y+1, len(place[0])):

        if place[x][i] == 1:
    
            place = lineup(place, x, y+1, x+1, i, 1)
            break
    
    for i in reversed(range(0, y)):

        if place[x][i] == 1 :
    
            place = lineup(place, x, i+1, x+1, y, 1)
            break

    return place


def removesticking(place, x, y):

    place[x][y] = 0
    
    for i in range(x+1, len(place)):

        if place[i][y] == 1:
    
            place = removeline(place, x+1, y, i, y+1, 0)
            break
    
    for i in reversed(range(0, x)):
 
        if place[i][y] == 1:

            place = removeline(place, i+1, y, x, y+1, 0)
            break

    for i in range(y+1, len(place[0])):

        if place[x][i] == 1:
    
            place = removeline(place, x, y+1, x+1, i, 1)
            break
    
    for i in reversed(range(0, y)):

        if place[x][i] == 1 :
    
            place = removeline(place, x, i+1, x+1, y, 1)
            break

    return place


m, n, h = [int(x) for x in input().split()]

data = []
place = []
max_z = 0


for _ in range(h):
    r, c, t = map(int, input().split())
    data.append([r, c, t])

for _ in range(m):
    temp = []
    for _ in range(n):
        temp.append(0)
    place.append(temp)

for i in data:
    if i[2] == 0:
        place = sticking(place, i[0], i[1])

    if i[2] == 1:
        place = removesticking(place, i[0], i[1])

    tempmax = 0
    for j in place:
        for k in j:
            if k != 0:
                tempmax += 1
        
    max_z = max(max_z, tempmax)

tempmax = 0
for i in place:
    for j in i:
        if j != 0:
            tempmax += 1
        
final = tempmax
max_z = max(max_z, final)

print(max_z)
print(final)