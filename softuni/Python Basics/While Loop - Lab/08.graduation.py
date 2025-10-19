student_name = input()
grades = 1
sum_marks = 0
excluded = 0

while grades <= 12:
    next_mark = float(input())
    if 2 <= next_mark < 4:
        excluded += 1
        if excluded > 1:
            break
    elif 4 <= next_mark <= 6:
        sum_marks += next_mark
        grades += 1

average = sum_marks / 12

if grades >= 12:
    print(f"{student_name} graduated. Average grade: {average:.2f}")
else:
    print(f"{student_name} has been excluded at {grades} grade")
