n = int(input())
data = []
top_score = -1
bad_counter = 0
total_score = 0
time = 0

for _ in range(n):
    t, s = map(int, input().split())
    data.append([t, s])

for i in data:
    if top_score < i[1]:
        top_score = i[1]
        time = i[0]

    if i[1] == -1:
        bad_counter += 1

total_score = top_score - len(data) - (bad_counter * 2)

if total_score < 0:
    print(0, time)
else:
    print(total_score, time)

