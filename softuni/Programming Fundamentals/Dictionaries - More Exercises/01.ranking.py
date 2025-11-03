contest_info = input()
contests_data = {}

while contest_info != "end of contests":
    contest_name, password = contest_info.split(":")
    contests_data[contest_name] = password

    contest_info = input()

submission_info = input()
users_data = {}

while submission_info != "end of submissions":
    contest, passw, username, points = submission_info.split("=>")
    points = int(points)
    
    if contest in contests_data and contests_data[contest] == passw:
        if username not in users_data:
            users_data[username] = {}

        if contest not in users_data[username]:
            users_data[username][contest] = points
        else:
            users_data[username][contest] = max(users_data[username][contest], points)

    submission_info = input()

best_user = ""
max_points = 0

for user, info in users_data.items():
    user_points = sum(info.values())
        
    if user_points > max_points:
        max_points = user_points
        best_user = user
    
print(f"Best candidate is {best_user} with total {max_points} points.\nRanking:")

for user in sorted(users_data.keys()):
    print(user)
    for course, points in sorted(users_data[user].items(), key=lambda x: -x[1]):
        print(f"#  {course} -> {points}")
        