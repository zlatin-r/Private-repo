info = input()
phonebook = {}

while not info.isdigit():
    name, number = info.split("-")

    phonebook[name] = number

    info = input()

for _ in range(int(info)):
    contact = input()

    if contact in phonebook:
        print(f"{contact} -> {phonebook[contact]}")
    else:
        print(f"Contact {contact} does not exist.")

