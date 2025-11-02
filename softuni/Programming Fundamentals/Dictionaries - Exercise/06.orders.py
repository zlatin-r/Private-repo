command = input()
data = {}

while command != "buy":
    token = command.split()
    product, price, quantity = token[0], float(token[1]), int(token[2])

    if product not in data:
        data[product] = {"price": 0.0, "quantity": 0}

    data[product]["price"] = price
    data[product]["quantity"] += quantity

    command = input()

for prod, info in data.items():
    total_price = info["price"] * info["quantity"]
    print(f"{prod} -> {total_price:.2f}")
