data = input().split(", ")

for el in data:
    if el == "0":
        data.remove(el)
        data.append(0)

print(data)
