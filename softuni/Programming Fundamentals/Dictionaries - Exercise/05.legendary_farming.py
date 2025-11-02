stack = {"shards": 0, "fragments": 0, "motes": 0}
legendary_items = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}
legendary_obtained = False

while not legendary_obtained:
    data = input().split()

    for i in range(0, len(data), 2):
        quant = int(data[i])
        material = data[i + 1].lower()

        if material not in stack:
            stack[material] = 0
        stack[material] += quant

        if stack["shards"] >= 250 or stack["fragments"] >= 250 or stack["motes"] >= 250:
            stack[material] -= 250
            print(f"{legendary_items[material]} obtained!")
            legendary_obtained = True
            break

for k, v in stack.items():
    print(f"{k}: {v}")
