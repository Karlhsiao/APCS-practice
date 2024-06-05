def count_city_beside(x, y, r, c):
    count = 4
    if x == 0:
        count -= 1

    if y == 0:
        count -= 1

    if x == c:
        count -= 1

    if y == r:
        count -= 1

    return count

def calculate_base(x, y):
    

    


r, c, k, m = [int(x) for x in input().split()]
print(r, c, k, m)

data = []

for _ in range(r):
    temp = [int(x) for x in input().split()]
    
    data.append(temp)

print(data)

