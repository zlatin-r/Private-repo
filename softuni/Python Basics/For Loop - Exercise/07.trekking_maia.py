n = int(input())

musala = 0
mont_blanc = 0
kilimanjaro = 0
k2 = 0
everest = 0
total_climbers = 0

for _ in range(n):
    group = int(input())

    if group <= 5:
        musala += group
    elif 6 <= group <= 12:
        mont_blanc += group
    elif 13 <= group <= 25:
        kilimanjaro += group
    elif 26 <= group <= 40:
        k2 += group
    elif 41 <= group:
        everest += group

    total_climbers += group

p1 = musala / total_climbers * 100
p2 = mont_blanc / total_climbers * 100
p3 = kilimanjaro / total_climbers * 100
p4 = k2 / total_climbers * 100
p5 = everest / total_climbers * 100

print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
print(f"{p4:.2f}%")
print(f"{p5:.2f}%")
