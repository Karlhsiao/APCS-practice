count = int(input())  
datas = []  
# 逐一讀取每個線段的起點與終點
for _ in range(count):
    start, end = map(int, input().split(" "))
    datas.append([start, end])
# 根據線段起點升序排列，如果起點相同則以終點升序排列
print(datas)
datas.sort(key=lambda x: (x[0], x[1]))
print(datas)
total = 0  
tempS = datas[0][0]  
tempE = datas[0][1]  
# 逐一處理每個線段
for i in range(1, len(datas)):
    # 如果該線段的起點比目前線段的終點還要後面，表示目前的線段已經無法延伸
    # 將目前的線段長度加到總長度中，並重新設定起點與終點
    if datas[i][0] > tempE:
        long = tempE - tempS
        total += long
        tempS = datas[i][0]
        tempE = datas[i][1]
        print(tempS, tempE)
    else:
        # 如果該線段的終點比目前線段的終點還要後面，表示目前的線段還可以延伸
        # 將目前的終點更新為該線段的終點
        if datas[i][1] > tempE:
            tempE = datas[i][1]
# 處理最後一個線段
long = tempE - tempS
total += long
print(total)  # 輸出未被覆蓋的線段總長度