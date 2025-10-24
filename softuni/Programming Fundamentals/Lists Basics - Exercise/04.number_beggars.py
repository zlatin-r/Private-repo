numbers = input().split(", ")
n = int(input())

sums = [0] * n

for i in range(len(numbers)):
    beggar_index = i % n
    sums[beggar_index] += int(numbers[i])

print(sums)
