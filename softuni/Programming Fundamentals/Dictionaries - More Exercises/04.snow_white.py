command = input()

data = {}

while command != "Once upon a time":
    name, color, physics = command.split(" <:> ")
    physics = int(physics)

    if color not in data:
        data[color] = {}

    if name in data[color]:
        if data[color][name] < physics:
            data[color][name] = physics
    else:
        data[color][name] = physics

    command = input()

flat_dwarfs = []
for color, dwarfs in data.items():
    for name, physics in dwarfs.items():
        flat_dwarfs.append((name, color, physics))

color_counts = {color: sum(len(d) for c, d in data.items() if c == color) for color in data}

flat_dwarfs.sort(key=lambda x: (-x[2], -color_counts[x[1]]))

for name, color, physics in flat_dwarfs:
    print(f"({color}) {name} <-> {physics}")
