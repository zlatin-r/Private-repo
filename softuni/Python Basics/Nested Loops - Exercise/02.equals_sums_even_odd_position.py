num1 = int(input())
num2 = int(input())

for n in range(num1, num2 + 1):

    parced_num = str(n)

    odd_sum = 0
    even_sum = 0

    for index, digit in enumerate(n):
        if index % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)

    if even_sum == odd_sum:
        print(n, end=" ")
