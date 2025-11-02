results = {}
submissions = {}

while True:
    command = input()
    if command == "exam finished":
        break

    data = command.split("-")

    if data[1] == "banned":
        username = data[0]
        if username in results:
            del results[username]
    else:
        username, language, points = data[0], data[1], int(data[2])

        if language not in submissions:
            submissions[language] = 0
        submissions[language] += 1

        if username not in results:
            results[username] = points
        else:
            results[username] = max(results[username], points)

print("Results:")
for user, pts in results.items():
    print(f"{user} | {pts}")

print("Submissions:")
for lang, count in submissions.items():
    print(f"{lang} - {count}")
