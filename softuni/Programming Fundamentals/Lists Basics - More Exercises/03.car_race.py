numbers = list(map(int, input().split(" ")))
mid_idx = len(numbers) // 2
racer_a = 0
racer_b = 0

for a in range(mid_idx):
    curr_time_a = numbers[a]

    if curr_time_a == 0:
        racer_a *= 0.80
    
    racer_a += curr_time_a

for b in range(len(numbers) - 1, mid_idx, -1):
    curr_time_b = numbers[b]

    if curr_time_b == 0:
        racer_b *= 0.80

    racer_b += curr_time_b

if racer_a < racer_b:
    print(f"The winner is left with total time: {racer_a:.1f}")
else:
    print(f"The winner is right with total time: {racer_b:.1f}")
