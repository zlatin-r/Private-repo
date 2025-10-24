fires = input().split("#")
water = int(input())

fire_lst = []
effort = 0
total_fire = 0

for fire in fires:
    level, value = fire.split(" = ")
    value = int(value)

    if ((level == "High" and 81 <= value <= 125) or \
        (level == "Medium" and 51 <= value <= 80) or \
        (level == "Low" and 1 <= value <= 50)) and water >= value:

        water -= value
        effort += value * 0.25
        total_fire += value
        fire_lst.append(value)

print(f"Cells:")
if fire_lst:
     print("\n".join(f"- {c}" for c in fire_lst))
print(f"Effort: {effort:.2f}\nTotal Fire: {total_fire}")
