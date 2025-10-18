speed = float(input())
message = ""

if speed <= 10:
    message = "slow"
elif 10 < speed <= 50:
    message = "average"
elif 50 < speed <= 150:
    message = "fast"
elif 150 < speed <= 1000:
    message = "ultra fast"
elif 1000 < speed:
    message = "extremely fast"

print(message)
