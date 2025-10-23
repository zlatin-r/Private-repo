n = int(input())
numbers = []

for _ in range(n):
    num = int(input())
    numbers.append(num)

command = input()

if command == "even":
    numbers = [n for n in numbers if n % 2 == 0]
elif command == "odd":
    numbers = [n for n in numbers if n % 2 != 0]
elif command == "negative":
    numbers = [n for n in numbers if n < 0]
elif command == "positive":
    numbers = [n for n in numbers if n >= 0]

print(numbers)
