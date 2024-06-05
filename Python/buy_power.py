n, d = [int(x) for x in input().split()]

total_price = 0
quantity = 0

for _ in range(n):
    temp = [int(x) for x in input().split()]
    temp = sorted(temp)
    if temp[-1] - temp[0] >= d:
        quantity += 1
        total_price += int((sum(temp)/3))

print(quantity, total_price)