count = int(input())
line_list = []

for _ in range(count):
    start, end = map(int, input().split())
    line_list.append([start, end])

line_list.sort(key=lambda x: (x[0], x[1]))

lineS = line_list[0][0]
lineE = line_list[0][1]
total = 0

for i in range(1, len(line_list)):
    if line_list[i][0] > lineE:
        total += lineE - lineS
        lineS = line_list[i][0]
        lineE = line_list[i][1]

    else:
        if lineE < line_list[i][1]:
            lineE = line_list[i][1]

total += lineE - lineS

print(total)
    