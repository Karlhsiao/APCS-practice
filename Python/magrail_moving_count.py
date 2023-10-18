inputstring = input()
ans = 0

while "L" in inputstring or "E" in inputstring:
    counter = 0

    for i in inputstring:
        if i == "L":
            L = counter
        if i == "E":
            E = counter
            break
            
        counter += 1

    if E - L == 4 or E - L == 3:

        inputstring = inputstring[:E] + inputstring[E+1:]
        inputstring = inputstring[:L] + inputstring[L+2:]

        continue


    firststring = inputstring[:L]

    bottomstring = inputstring[E+1:]

    inputstring = firststring + ( inputstring[L+2:E] * int(inputstring[L+1]) ) + bottomstring

liststring = inputstring.split("T")[1:]

for i in range(len(liststring) - 1):

        temp = int(liststring[i+1]) - int(liststring[i])

        ans += abs(temp)

print(ans)


