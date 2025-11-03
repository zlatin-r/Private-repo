command = input()

players_pool = {}

while command != "Season end":

    if "->" in command:
        player, position, skill = command.split(" -> ")
        skill = int(skill)

        if player not in players_pool:
            players_pool[player] = {position: skill}
        else:
            if position in players_pool[player]:
                players_pool[player][position] = max(players_pool[player][position], skill)
            else:
                players_pool[player][position] = skill

    elif "vs" in command:
        player_1, player_2 = command.split(" vs ")

        if player_1 in players_pool and player_2 in players_pool:
            positions1 = set(players_pool[player_1].keys())
            positions2 = set(players_pool[player_2].keys())
            common = positions1 & positions2

            if common:        
                skill_p1 = sum(players_pool[player_1].values())
                skill_p2 = sum(players_pool[player_2].values())

                if skill_p1 > skill_p2:
                    del players_pool[player_2]
                elif skill_p2 > skill_p1:
                    del players_pool[player_1]

    command = input()

sorted_pool = sorted(players_pool.items(), key=lambda x: (-sum(x[1].values()), x[0]))

for plyr, info in sorted_pool:
    total_skill = sum(info.values())
    print(f"{plyr}: {total_skill} skill")

    sorted_pos = sorted(info.items(), key=lambda x: (-x[1], x[0]))
    for pos, points in sorted_pos:
        print(f"- {pos} <::> {points}")
