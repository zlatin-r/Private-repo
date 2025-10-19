money_needed = float(input())
money_have = float(input())
days_spend = 0
total_days = 0

while True:
    acton = input()
    amount = float(input())

    total_days += 1

    if acton == "spend":
        days_spend += 1

        if days_spend == 5:
            print(f"You can't save the money.\n{days_spend}")
            break

        money_have -= amount

        if money_have < 0:
            money_have = 0
        
    if acton == "save":
        money_have += amount

        if money_have >= money_needed:
            print(f"You saved the money for {total_days} days.")
            break
