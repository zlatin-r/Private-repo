n = int(input()) * 2

left_sum = 0
rigth_sum = 0

for i in range(n):
    number = int(input())
    if i < n / 2:
        left_sum += number
    else:
        rigth_sum += number

if left_sum == rigth_sum:
    print(f"Yes, sum = {left_sum}")
else:
    diff = abs(left_sum - rigth_sum)
    print(f"No, diff = {diff}")
