from sys import stdin

def unrotate(array):
    nlist = []
    n = -1

    for _ in range(len(array[0])):
        rlist = []
        for i in array:
            rlist.append(i[n])

        nlist.append(rlist)    
        n -= 1
        
    return nlist

def unflip(array):
    array.reverse()
      
    return array

ans = []

while 1:
    try:
        array = []

        R, C, M = input().split()

        for _ in range(int(R)):
            array.append(input().split())

        k = [int(x) for x in input().split()]
        k.reverse()

        for i in k:
            if i == 1:
                array = unflip(array)

            elif i == 0:
                array = unrotate(array)

        ans.append([len(array), len(array[0])])
        ans += array

    except:
        break

ret = ""

for i in ans:
    for j in i:
        ret += str(j) + " "

    print(ret.rstrip())
    ret = ""
