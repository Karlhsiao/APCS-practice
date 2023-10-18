def inner_dot(a, b, i, j, r, revA, revB):

    ls1 = a.copy()
    ls2 = b.copy()

    if len(a) < i + r:
        raise Exception("a<i+r")

    if len(b) < i + r:
        raise Exception("b<i+r")
    
    if len(a) < r:
        raise Exception("a<r")

    if len(b) < r:
        raise Exception("b<r")
    '''
    if type(a) != "list" or type(b) != "list":
        raise Exception("a or b TypeError")

    if type(i) != "integer" or type(j) != "integer":
        raise Exception("i or j TypeError")
    
    if type(r) != "integer":
        raise Exception("r TypeError")

    if type(revA) != "integer" or type(revB) != "integer":
        raise Exception("i or j TypeError")
    '''
    if r < 0:
        raise Exception("r<0")
    
    if revA < 0 or revA > 1:
        raise Exception("revA range error")
    
    if revB < 0 or revB > 1:
        raise Exception("revB range error")
 

    if revA == 1:
        ls1.reverse()

    if revB == 1:
        ls2.reverse()
    
    ans = 0

    for n in range(r):
        ans += ls1[i+n]*ls2[j+n]

    return ans


n, m = map(int, input().split())

ls1 = [int(x) for x in input().split()]
ls2 = [int(x) for x in input().split()]

max_num = 0

temp = 0

for i in range(0, n):
    for j in range(0, m):
        temp = max(ls1[i] * ls2[j] + temp, ls1[i] * ls2[j])
        max_num = max(max_num, temp)
        print(temp)


print(temp)
