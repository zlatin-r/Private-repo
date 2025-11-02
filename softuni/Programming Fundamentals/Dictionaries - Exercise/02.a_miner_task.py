command = input()
data = {}

while command != "stop":
    quantity = int(input())
    
    if command not in data:
        data[command] = 0
    data[command] += quantity

    command = input()

for r, q in data.items():
    print(f"{r} -> {q}")
