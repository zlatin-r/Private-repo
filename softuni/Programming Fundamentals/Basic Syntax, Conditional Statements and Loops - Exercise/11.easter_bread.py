budget = float(input())
flour_price = float(input())
eggs_price = flour_price * 0.75
milk_price = (flour_price * 1.25) / 4

bread_price = flour_price + eggs_price + milk_price

curr_bread_count = 0
colored_eggs = 0

while budget > bread_price:
    colored_eggs += 3
    curr_bread_count += 1

    if curr_bread_count % 3 == 0:
        colored_eggs -= curr_bread_count - 2

    budget -= bread_price
    
print(f"You made {curr_bread_count} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
