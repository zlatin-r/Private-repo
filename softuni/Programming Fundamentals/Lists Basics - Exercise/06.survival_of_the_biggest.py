numbers = list(map(int, input().split(" ")))
n = int(input())

for _ in range(n):
    numbers.remove(min(numbers))

print(", ".join(str(num) for num in numbers))
