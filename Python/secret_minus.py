num = input()
odd = 0
even = 0

for i in range(len(num)):
    if i % 2 != 0:
        odd += int(num[i])

    elif i % 2 == 0:
        even += int(num[i])

print(abs(odd - even))
