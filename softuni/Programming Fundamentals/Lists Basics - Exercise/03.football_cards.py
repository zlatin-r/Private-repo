commands = input().split(" ")

a_team = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]
b_team = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]
terminated = False

for c in commands:
    team, player = c.split("-")

    if team == "A":
        if player in a_team:
            a_team.remove(player)

    if team == "B":
        if player in b_team:
            b_team.remove(player)
            
    if len(a_team) < 7 or len(b_team) < 7:
        terminated = True
        break

print(f"Team A - {len(a_team)}; Team B - {len(b_team)}")

if terminated:
    print("Game was terminated")
