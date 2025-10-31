command = input()

products = {}

while command != "statistics":
    product, quantity = command.split(":")

    if product in products:
        products[product] += int(quantity)
    else:
        products[product] = int(quantity)

    command = input()

print("Products in stock:\n" + "\n".join([f"- {p}: {q}" for p, q in products.items()]))
print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")
