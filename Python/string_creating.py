def insert_char(string, numlist):
    templist = [""]*len(numlist)
    newstring = ""

    for i in range(len(numlist)):
        templist[numlist[i]-1] = string[i]

    for i in templist:
        newstring += i

    return newstring



k, q, r = [int(x) for x in input().split()]

string = input()

anslist = []
finalstring = ""
num = []


for _ in range(q):
    temp = [int(x) for x in input().split()]
    num.append(temp)
    
print(num)

for i in num:
    string = insert_char(string, i)
    anslist.append(string)

print(anslist)


for i in range(r):
    for j in range(q):
        finalstring += anslist[j][i]

    print(finalstring)
    finalstring = ""
    
    