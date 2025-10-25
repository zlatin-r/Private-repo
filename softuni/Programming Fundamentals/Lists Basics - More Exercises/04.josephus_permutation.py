people = list(map(int, input().split(" ")))
k = int(input())

result = []
index = 0

while people:
    index = (index + k - 1) % len(people)
    result.append(people.pop(index))

print(f"[{','.join(map(str, result))}]")
