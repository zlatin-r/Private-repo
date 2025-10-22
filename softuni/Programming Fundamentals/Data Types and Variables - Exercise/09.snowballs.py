n = int(input())
max_value = 0
message = ""

for _ in range(n):
    weight = int(input())
    time = int(input())
    quality = int(input())

    value = (weight // time) ** quality

    if value > max_value:
        max_value = value
        message = f"{weight} : {time} = {value} ({quality})"

print(message)
