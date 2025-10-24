data = input().split("|") 
budget = float(input())

ticket = 150
new_prices = []
profit = 0

for info in data:
    item, price = info.split("->")
    price = float(price)

    if ((item == "Clothes" and price <= 50) or \
        (item == "Shoes" and price <= 35) or \
        (item == "Accessories" and price <= 20.50)) and budget >= price:
        budget -= price
        new_price = price * 1.40
        new_prices.append(new_price) 
        profit += new_price - price

print(" ".join(f"{p:.2f}" for p in new_prices))
print(f"Profit: {profit:.2f}")

if budget + sum(new_prices) >= ticket:
    print("Hello, France!")
else:
    print("Not enough money.")
