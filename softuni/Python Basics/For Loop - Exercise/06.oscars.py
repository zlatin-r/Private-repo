actor_name = input()
actor_points = float(input())
n = int(input())

points_needed = 1250.5

for _ in range(n):
    jury_name = input()
    points = float(input())

    actor_points += (len(jury_name) * points) / 2

    if actor_points >= points_needed:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {actor_points:.1f}!")
        break

if actor_points < points_needed:
    diff = points_needed - actor_points
    print(f"Sorry, {actor_name} you need {diff:.1f} more!")
