note_list = [0] * 10

while True:
    command = input()

    if command == "End":
        break
    
    tokens = command.split("-")
    priopity = int(tokens[0] - 1)
    note = tokens[1]

    note_list.pop(priopity)
    note_list.insert(priopity, note)

note_list = [el for el in note_list if el != 0]
print(note_list)
