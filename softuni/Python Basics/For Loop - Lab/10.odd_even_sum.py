n = int(input())

odd_sum = 0
even_sum = 0

for i in range(0, n):
    number = int(input())
    if i % 2 == 0:
        even_sum += number
    else:
        odd_sum += number

if even_sum == odd_sum:
    print(f"Yes\nSum = {odd_sum}")
else:
    print(f"No\nDiff = {abs(even_sum-odd_sum)}")
