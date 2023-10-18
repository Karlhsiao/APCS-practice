total = 0
win = 0
lose = 0

for _ in range(2):
    game = [int(x) for x in input().split()]
    team1 = 0

    for i in game:
        team1 += i

    game2 = [int(x) for x in input().split()]
    team2 = 0

    for i in game2:
        team2 += i
    
    if team1 > team2:
        win = 1

    if team1 < team2:
        lose = 1

    print(f"{team1}:{team2}")

if win == lose:
    print("Tie")

elif win > lose:
    print("Win")

elif win < lose:
    print("Lose")