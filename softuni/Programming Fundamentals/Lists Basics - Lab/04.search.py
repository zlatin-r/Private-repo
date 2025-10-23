n = int(input())
word = input()

result = []

for _ in range(n):
    data = input()

    result.append(data)

print(result)
result = [s for s in result if word in s]
print(result)
