vagons = int(input())
train  = [0] * vagons

command = input()

while command != "End":
    data = command.split()
    action = data[0]

    if action == "add":
        people = int(data[1])
        train[vagons -1] += people
    elif action == "insert":
        index, people = int(data[1]), int(data[2])
        train[index] += people
    elif action == "leave":
        index, people = int(data[1]), int(data[2])
        train[index] -= people

    command = input()

print(train)
