from sys import stdin

for i in stdin:
    ans = ""
    n = int(i)

    for _ in range(int(n)):
        code = stdin.readline().strip()

        if code == "0 1 0 1":
            ans += "A"

        elif code == "0 1 1 1":
            ans += "B" 

        elif code == "0 0 1 0":
            ans += "C"

        elif code == "1 1 0 1":
            ans += "D"

        elif code == "1 0 0 0":
            ans += "E"

        elif code == "1 1 0 0":
            ans += "F"
        
    print(ans)
    

