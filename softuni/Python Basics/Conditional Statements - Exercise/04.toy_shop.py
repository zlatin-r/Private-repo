puzzle_price = 2.6
doll_price = 3
teddy_bear_price = 4.1
minion_price = 8.2
truck_price = 2
discount = 0.25
rent = 0.1

excursion_price = float(input())

num_puzzles = int(input())
num_dolls = int(input())
num_teddy_bears = int(input())
num_minions = int(input())
num_trucks = int(input())

total_toys_ordered = num_puzzles + num_dolls + num_teddy_bears + num_minions + num_trucks

money = (num_puzzles * puzzle_price) + (num_dolls * doll_price) + (num_teddy_bears * teddy_bear_price) + (num_minions * minion_price) + (num_trucks * truck_price)

if total_toys_ordered >= 50:
    money -= money * discount

money -= money * rent

if excursion_price <= money:
    rest_money = money - excursion_price
    print(f"Yes! {rest_money:.2f} lv left.")
else:
    money_needed = excursion_price - money
    print(f"Not enough money! {money_needed:.2f} lv needed.")
