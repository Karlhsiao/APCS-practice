def reverse_string(string):
    half = int(len(string)/2)

    if len(string)/2 % 2 != 0:
        string = string[half+1:] + string[half] + string[:half]

    else:
        string = string[half:] + string[:half]

    return string

def revert_string(string, number):
    numlist = []
    strlist = []
    ans = []
    ansstring = ""

    for i in number:
        numlist.append(i)

    for i in string:
        strlist.append(i) 

    numlist.reverse()
    strlist.reverse()

    for i in range(len(numlist)):
        if numlist[i] == "0":
            ans.append(strlist[i])

        elif numlist[i] == "1":
            ans.insert(0, strlist[i])
    
    ans.reverse()

    for i in ans:
        ansstring += i

    return ansstring


m, n = [int(x) for x in input().split()]
data = []


for _ in range(m):
    data.append(input())

data.reverse()

string = input()

for i in data:
    string = revert_string(string, i)

    if i.count("1") % 2 != 0:
        string = reverse_string(string)
        
    

print(string)