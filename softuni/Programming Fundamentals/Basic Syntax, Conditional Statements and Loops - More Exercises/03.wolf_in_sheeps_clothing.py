data = input().split(", ")

for index, string in enumerate(data):
    if string == "wolf": 
        if index == len(data) - 1:
            print("Please go away and stop eating my sheep")
        else:
            sheep_num = len(data) - index - 1
            print(f"Oi! Sheep number {sheep_num}! You are about to be eaten by a wolf!")
