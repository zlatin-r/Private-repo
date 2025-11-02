n = int(input())
data = {}

for _ in range(n):
    name = input()
    grade = float(input())

    if name not in data:
        data[name] = []
    data[name].append(grade)

for student, grades in data.items():
    avg_grade = sum(grades) / len(grades)

    if avg_grade >= 4.50:
        print(f"{student} -> {avg_grade:.2f}")    
