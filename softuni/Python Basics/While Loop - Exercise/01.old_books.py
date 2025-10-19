target = input()

count = 0

while True:
    guess = input()

    if guess == target:
        print(f"You checked {count} books and found it.")
        break
    elif guess == "No More Books":
        print(f"The book you search is not here!\nYou checked {count} books.")
        break

    count += 1
