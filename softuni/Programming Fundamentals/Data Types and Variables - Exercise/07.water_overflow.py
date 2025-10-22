n = int(input())
amount_water = 0
capacity = 255

for i in range(n):
    water = int(input())

    if amount_water + water > capacity:
        print("Insufficient capacity!")
        continue
    else:
        amount_water += water

print(amount_water)
