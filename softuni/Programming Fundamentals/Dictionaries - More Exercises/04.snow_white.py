command = input()

data = {}

while command != "Once upon a time":
    name, color, physics = command.split(" <:> ")
    physics = int(physics)

    if color in data and name in data[color]:
        data[color][name] = max(data[color][name], physics)

    if color not in data:
        data[color] = {}

    if name not in data[color]:
        data[color][name] = physics
    
    command = input()

sorted_data = sorted(data.items(), key=lambda x: -sum(x[1].values()))

for col, info in sorted_data:
    for name, points in info.items():
        print(f"({col}) {name} <-> {points}")
