command = input()

data = {}
individual = {}

while command != "no more time":
    username, contest, points = command.split(" -> ")
    points = int(points)

    if contest not in data:
        data[contest] = {}

    if username not in data[contest]:
        data[contest][username] = points
    else:
        data[contest][username] = max(data[contest][username], points)

    command = input()

for contest, info in data.items():
    print(f"{contest}: {len(info)} participants")
    sorted_users = sorted(info.items(), key=lambda x: (-x[1], x[0]))

    for i, (user, points) in enumerate(sorted_users, 1):
        print(f"{i}. {user} <::> {points}")

print("Individual standings:")

for contest in data.values():
    for user, pts in contest.items():
        individual[user] = individual.get(user, 0) + pts

sorted_individuals = sorted(individual.items(), key=lambda x: (-x[1], x[0]))
for i, (user, points) in enumerate(sorted_individuals, 1):
    print(f"{i}. {user} -> {points}")
