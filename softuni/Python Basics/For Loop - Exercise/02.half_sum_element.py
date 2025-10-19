n = int(input())

total_sum = 0
biggest_num = 0

for _ in range(0, n):
    number = int(input())

    if biggest_num < number:
        biggest_num = number

    total_sum += number

if biggest_num == total_sum - biggest_num:
    print(f"Yes\nSum = {biggest_num}")
else:
    print(f"No\nDiff = {abs(biggest_num - (total_sum - biggest_num))}")
