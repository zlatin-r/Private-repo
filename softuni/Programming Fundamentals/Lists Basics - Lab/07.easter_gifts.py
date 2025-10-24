gifts = input().split(" ")
command = input()

while command != "No Money":
    data = command.split(" ")
    action, gift = data[0], data[1]

    if action == "OutOfStock":
        if gift in gifts:
            gifts = ["None" if x == gift else x for x in gifts]
    
    elif action == "Required":
        index = int(data[2])
      
        if 0 <= index < len(gifts):
            gifts[index] = gift
    
    elif action == "JustInCase":
        gifts[-1] = gift

    command = input()

filtered = [x for x in gifts if x != "None"]

print(" ".join(filtered))
