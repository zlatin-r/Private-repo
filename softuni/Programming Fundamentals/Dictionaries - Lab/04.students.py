info = input()
data = {}

while ":" in info:
    name, pid, course = info.split(":")
    data[pid] = [name, course]

    info = input()

course_name = info.replace("_", " ").lower()

for pid, (name, course) in data.items():
    if course.lower() == course_name:
        print(f"{name} - {pid}")
