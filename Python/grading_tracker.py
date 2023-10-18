people = input()
grades = [int(x) for x in input().split()]
luckycase = 100
unluckycase = 0
bestcases = False
grades = sorted(grades)
final = ""
best = 0
worst = 0

for i in grades:
    final += str(i) + " "

print(final.strip())

if grades[0] >= 60:
    best = 1

if grades[-1] < 60:
    worst = 1



for i in range(int(people)):
    if (luckycase > grades[i] and grades[i] >= 60):
        luckycase = grades[i]

    if (unluckycase < grades[i] and grades[i] < 60):
        unluckycase = grades[i]


if best == 1:
    print("best case")

else:
    print(unluckycase)


if worst == 1:
    print("worst case")

else:
    print(luckycase)



