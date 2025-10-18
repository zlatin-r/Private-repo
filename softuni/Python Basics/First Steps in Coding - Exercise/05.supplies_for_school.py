pack_pencil_price = 5.8
pack_marker_price = 7.2
detergent_price = 1.2

num_pencil_packs = int(input())
num_marker_packs = int(input())
litters_detergent = int(input())
discount_percentage = int(input()) / 100

total_price = ((num_pencil_packs * pack_pencil_price) + (num_marker_packs * pack_marker_price) + (litters_detergent * detergent_price))
price_with_discout = total_price - (total_price * discount_percentage)

print(price_with_discout)
