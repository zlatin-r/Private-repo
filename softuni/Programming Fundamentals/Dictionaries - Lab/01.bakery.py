data = input().split()

result = {}

for i in range(0, len(data), 2):
    result[data[i]] = int(data[i + 1])

print(result)
