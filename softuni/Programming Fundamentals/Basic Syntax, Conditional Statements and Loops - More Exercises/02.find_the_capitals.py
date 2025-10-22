word = input()
result = []

for index, letter in enumerate(word):
    if letter.isupper():
        result.append(index)

print(result)
