n = int(input())

w = input().split()
times = input().split()

data = []
dp = []
ans = 0

for i in range(n):
    tmpw, tmptimes = int(w[i]), int(times[i])
    data.append([tmpw, tmptimes])

data.sort(key=lambda x: x[0] * x[1])
temp = 0

k = 0

for _ in range(len(data)):

    i = 1
    while (i < len(data)-k):

        if data[i-1][0] * data[i][1] > data[i-1][1] * data[i][0]:
                data[i-1], data[i] = data[i], data[i-1]
        i += 1
    
    k += 1

for i in data:
    temp += i[0]
    dp.append(temp)

dp.insert(0, 0)

for i in range(len(data)):
    ans = ans + dp[i] * data[i][1]

print(ans)