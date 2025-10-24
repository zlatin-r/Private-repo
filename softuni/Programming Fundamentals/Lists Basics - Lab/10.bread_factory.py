events = input().split("|")

curr_energy = 100
coins = 100
day_completed = True

for event in events:
    event_name, number = event.split("-")
    number = int(number)

    if event_name == "rest":
        gained_energy = min(number, 100 - curr_energy)
        curr_energy += gained_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {curr_energy}.")
        
    elif event_name == "order":
        if curr_energy >= 30:
            coins += number
            curr_energy -= 30
            print(f"You earned {number} coins.")
        else:
            curr_energy = min(curr_energy + 50, 100)
            print("You had to rest!")
            
    else:
        if coins >= number:
            coins -= number
            print(f"You bought {event_name}.")
        else:
            print(f"Closed! Cannot afford {event_name}.")
            day_completed = False
            break

if day_completed:
    print(f"Day completed!\nCoins: {coins}\nEnergy: {curr_energy}")
    