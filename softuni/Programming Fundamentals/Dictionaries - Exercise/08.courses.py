info = input()
data = {}

while info != "end":
    tokens = info.split(" : ")
    course, student = tokens[0], tokens[1]

    if course not in data:
        data[course] = []
    data[course].append(student)

    info = input()

for course, students in data.items():
    print(f"{course}: {len(students)}")
    
    for student in students:
        print(f"-- {student}")
