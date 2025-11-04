n = int(input())

data = {}

for _ in range(n):
    dr_type, dr_name, damage, health, armor = input().split()

    health = 250 if health == "null" else int(health)
    damage = 45 if damage == "null" else int(damage)
    armor = 10 if armor == "null" else int(armor)

    if dr_type not in data:
        data[dr_type] = {}

    data[dr_type][dr_name] = {
        "health": health,
        "damage": damage,
        "armor": armor
    }

for dr_type, dragons in data.items():
    avg_damage = sum(d["damage"] for d in dragons.values()) / len(dragons)
    avg_health = sum(d["health"] for d in dragons.values()) / len(dragons)
    avg_armor = sum(d["armor"] for d in dragons.values()) / len(dragons)

    print(f"{dr_type}::({avg_damage:.2f}/{avg_health:.2f}/{avg_armor:.2f})")

    for name, stats in sorted(dragons.items()):
            print(f"-{name} -> damage: {stats['damage']}, health: {stats['health']}, armor: {stats['armor']}")
