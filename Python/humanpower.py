a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

n = int(input())

i = 0
max_profit = None

while i <= n:
    profit1 = a1 * i**2 + b1 * i + c1
    profit2 = a2 * (n-i)**2 + b2 * (n-i) + c2
    total_profit = profit1 + profit2

    if max_profit == None:
        max_profit = total_profit

    max_profit = max(total_profit, max_profit)

    i += 1

print(max_profit)