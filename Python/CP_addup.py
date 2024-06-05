m, n = map(int, input().split())

cp_data = dict()
data = []
all_itemlist = []
ans = 0
 
for _ in range(n):
    k = 0
    for i in input():
        if i in cp_data:
            cp_data.update({i : cp_data.get(i)+1})

        else:
            cp_data.update({i : 1})
            all_itemlist.append(i)

        if k >= m:
            break
            
        k += 1
    data.append(cp_data)
    cp_data = {}

all_itemlist = set(all_itemlist)

#print(data)
#print(all_itemlist)

for i in data:
    for j in data:
        #print(i.keys(), j.keys(), i.keys() ^ j.keys())
        if i.keys() ^ j.keys() == all_itemlist:
            ans += 1

print(ans//2)