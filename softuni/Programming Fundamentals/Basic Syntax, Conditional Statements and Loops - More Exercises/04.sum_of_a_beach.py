string = input().lower()

searched_words = ["sand", "water", "fish", "sun"]
counter = 0

for word in searched_words:
    counter += string.count(word)

print(counter)
