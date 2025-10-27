product = input()
quantity = int(input())

def solve(pr, qu):
    price = 0

    if pr == "coffee":
        price = 1.5
    elif pr == "coke":
        price = 1.4
    elif pr == "water":
        price = 1
    elif pr == "snacks":
        price = 2

    return f"{(price * qu):.2f}"

print(solve(product, quantity))
