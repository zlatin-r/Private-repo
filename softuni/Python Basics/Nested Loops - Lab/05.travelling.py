while True:
    destination = input()

    if destination == "End":
        break
        
    budget = float(input())

    while budget:
        money = float(input())
        budget -= money
        
        if budget <= 0:
            print(f"Going to {destination}!")
            break
