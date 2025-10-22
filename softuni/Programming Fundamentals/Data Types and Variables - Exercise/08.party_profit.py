from math import floor

group_size = int(input())
days = int(input())

total_coins = 0

for d in range(1, days + 1):
    total_coins += 50

    if d % 10 == 0:
        group_size -= 2

    if d % 15 == 0:
        group_size += 5

    total_coins -= group_size * 2

    if d % 3 == 0:
        total_coins -= group_size * 3

    if d % 5 == 0:
        total_coins += group_size * 20
        if d % 3 == 0:
            total_coins -= group_size * 2

coins_rep_companion = floor(total_coins / group_size)

print(f"{group_size} companions received {coins_rep_companion} coins each.")
