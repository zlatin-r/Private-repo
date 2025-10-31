data = input().split()
searched_products = input().split()

products = {}

for i in range(0, len(data), 2):
    products[data[i]] = data[i + 1]

for product in searched_products:
    if product in products.keys():
        print(f"We have {products[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
