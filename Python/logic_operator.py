def an(x, y):
    if x>0 and y>0:
        return 1
    
    else:
        return 0

def orr(x, y):
    if x>0 or y>0:
        return 1
    
    else:
        return 0

def xor(x, y):
    if orr(x, y):
        if an(x, y):
            return 0
        
        else:
            return 1

    else:
        return 0

a, b, c = [int(x) for x in input().split()]
imp = 1

if an(a, b) == c:
    print("AND")
    imp = 0

if orr(a, b) == c:
    print("OR")
    imp = 0

if xor(a, b) == c:
    print("XOR")
    imp = 0

if imp == 1:
    print("IMPOSSIBLE")
