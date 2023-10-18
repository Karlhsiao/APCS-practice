n, m = input().split()
data = []
total = 0
data_top = []
string = ""

for _ in range(int(n)):
    temp = input().split()
    temp = [int(x) for x in temp]
    temp.sort()
    data.append(temp)

for i in range(len(data)):
    total += int(data[i][-1])
    data_top.append(int(data[i][-1]))

print(total)

for i in data_top:
    if total % i == 0:
        string += str(i) + " "

if string == "":
    print(-1)
else:
    print(string.rstrip())
