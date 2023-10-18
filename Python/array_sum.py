def sum_dif(arr1, arr2):
    sum1 = 0
    sum2 = 0
    ans = 0

    for i in range(arr1):
        for j in range(arr1[0]):
            sum1 += arr1[i][j]
            sum2 += arr2[i][j]
    
    ans = abs(sum1 + sum2)

    return ans


s, t, n, m, r = map(int, input().split())

smol_array = []
big_array = []
diff_counter = 0
lowest_r = -1
ans = 0
hit = 0

for _ in range(s):
    smol_array.append([int(x) for x in input().split()])

for _ in range(n):
    big_array.append([int(x) for x in input().split()])

for i in range(0, n-s+1):
    
    for j in range(0, m-t+1):
        
        for k in range(s):
            
            for n in range(t):

                print(smol_array[k][n], big_array[k+i][n+j])
                if smol_array[k][n] != big_array[k+i][n+j]:
                    diff_counter += 1
                    
                if diff_counter > r:
                    print("dead\n")
                    break

            if diff_counter > r:
                
                break

        if diff_counter > r:
            diff_counter = 0

        elif diff_counter <= r:
            print("pass\n")

            lowest_r = min(lowest_r, hit)

print(ans)
print(lowest_r)