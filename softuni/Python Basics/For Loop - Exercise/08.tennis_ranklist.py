from math import floor

n = int(input())
start_points = int(input())
bonus_points = 0
wins = 0

for _ in range(n):
    stage = input()

    if stage == "W":
        wins += 1
        bonus_points += 2000
    elif stage == "F":
        bonus_points += 1200
    elif stage == "SF":
        bonus_points += 720

avg_points = bonus_points / n
avg_win_percents = (wins / n) * 100

print(f"Final points: {bonus_points + start_points}")
print(f"Average points: {floor(avg_points)}")
print(f"{avg_win_percents:.2f}%")
