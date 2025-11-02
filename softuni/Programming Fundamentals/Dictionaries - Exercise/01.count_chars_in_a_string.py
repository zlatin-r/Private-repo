string = input()
data = {}

for word in string:
    for letter in list(word):
        if letter not in data:
            data[letter] = 0
        data[letter] += 1

for k, v in data.items():
    print(f"{k} -> {v}")
