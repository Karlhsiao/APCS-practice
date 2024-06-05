n, d = map(int, input().split())

data = [int(x) for x in input().split()]

own = 0
last_deal = 0
stockp = 0
profit = 0
first = 1

for i in data:
    if first == 1:
        first = 0
        own = 1
        last_deal = i

    elif own == 0:
        if i <= last_deal - d:
            own = 1
            last_deal = i

    else:
        if i >= last_deal + d:
            own = 0
            profit += i - last_deal
            last_deal = i


print(profit) 