chicken_menu_price = 10.35
fish_menu_price = 12.4
vegi_menu_price = 8.15
delivery_price = 2.5

num_chicken_menus = int(input())
num_fish_menus = int(input())
num_vegi_menus = int(input())

total_chicken_menu_price = chicken_menu_price * num_chicken_menus
total_fish_menu_price = fish_menu_price * num_fish_menus
total_vegi_menu_price = vegi_menu_price * num_vegi_menus

total_menu_price = total_chicken_menu_price + total_fish_menu_price + total_vegi_menu_price

dessert_price = total_menu_price * 0.20

total_price = total_menu_price + dessert_price + delivery_price

print(f"{total_price:.2f}")
