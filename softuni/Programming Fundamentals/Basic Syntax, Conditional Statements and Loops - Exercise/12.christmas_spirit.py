quantity = int(input())
days = int(input())

ornament_set_price = 2
ornament_set_points = 5
tree_skirt_price = 5
tree_skirt_points = 3
tree_garland_price = 3
tree_garland_points = 10
tree_lights_price = 15
tree_lithts_points = 17

spirit_points = 0
total_costs = 0

for d in range(1, days + 1):

    if d % 11 == 0:
        quantity += 2

    if d % 2 == 0:
        total_costs += ornament_set_price * quantity
        spirit_points += ornament_set_points

    if d % 3 == 0:
        total_costs += (tree_skirt_price + tree_garland_price) * quantity
        spirit_points += tree_skirt_points + tree_garland_points

    if d % 5 == 0:
        total_costs += tree_lights_price * quantity
        spirit_points += tree_lithts_points

    if d % 3 == 0 and d % 5 == 0:
        spirit_points += 30

    if d % 10 == 0:
        total_costs += tree_skirt_price + tree_garland_price + tree_lights_price
        spirit_points -= 20


if days % 10 == 0:
    spirit_points -= 30

print(f"Total cost: {total_costs}")
print(f"Total spirit: {spirit_points}")
