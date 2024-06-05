n = int(input())
data = []
for _ in range(n):
    a, b = map(int, input().split())
    data.append([a, b])
data.sort(key=lambda data: data[0]**2 + data[1]**2)
print(data[-2][0], data[-2][1])

