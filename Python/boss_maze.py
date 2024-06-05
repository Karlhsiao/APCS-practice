def allbossesdead(bosses):
    dead = True
    if len(bosses) >= 1:
        dead = False
        
    return dead

def cleardeadboss(bosses, map=None):
    alive_boss = []
    for i in bosses:
        if i[4] == 1:
            alive_boss.append(i)
        
        if map != None:
            if i[4] == 0:
                map[i[0]-i[2]][i[1]-i[3]] = 1

    if map == None:
        return alive_boss
    
    else:
        return alive_boss, map

n, m, k = map(int, input().split())

bomb_map = []
bosses = []
ans = 0
deadboss = [0, 0, 0, 0, 0]

for _ in range(n):
    temp = []
    for _ in range(m):
        temp.append(0)
    bomb_map.append(temp)

for _ in range(k):
    r, c, s, t = map(int, input().split())
    bosses.append([r, c, s, t, 1])

while not allbossesdead(bosses):
    for i in bosses:
        bomb_map[i[0]][i[1]] = 1
    
    for i in range(len(bosses)):
        
        if bosses[i][0] + bosses[i][2] > len(bomb_map)-1:

            bosses[i][4] = 0
        
        elif bosses[i][0] + bosses[i][2] < 0:

            bosses[i][4] = 0
        
        if bosses[i][1] + bosses[i][3] > len(bomb_map[0])-1:

            bosses[i][4] = 0
        
        elif bosses[i][1] + bosses[i][3] < 0:
            
            bosses[i][4] = 0
            

        bosses[i][0] += bosses[i][2]
        bosses[i][1] += bosses[i][3]
    
    bosses, bomb_map = cleardeadboss(bosses, bomb_map)
    
    for i in range(len(bosses)):

        if bomb_map[bosses[i][0]][bosses[i][1]] == 1 or bomb_map[bosses[i][0]][bosses[i][1]] == 3:
            bosses[i][4] = 0
            bomb_map[bosses[i][0]][bosses[i][1]] = 3
    
    for i in range(len(bomb_map)):
        for j in range(len(bomb_map[0])):
            if bomb_map[i][j] == 3:
                bomb_map[i][j] = 0

    bosses = cleardeadboss(bosses)

for i in bomb_map:
    for j in i:
        if j != 0:
            ans += 1

print(ans)
    
                
