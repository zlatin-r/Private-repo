budget = float(input())
extra = int(input())
cost_clouthing = float(input())

set_design = budget * 0.1

if extra > 150:
    cost_clouthing -= cost_clouthing * 0.1

total_cost = (extra * cost_clouthing) + set_design

if total_cost > budget:
    money_needed = total_cost - budget
    print("Not enough money!")
    print(f"Wingard needs {money_needed:.2f} leva more.")
else:
    money_rest = budget - total_cost
    print("Action!")
    print(f"Wingard starts filming with {money_rest:.2f} leva left.")
