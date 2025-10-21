n = int(input())
command = input()

total_score = 0
counter = 0

while command != "Finish":

    avg_score = 0
    sum = 0

    for _ in range(n):
        grade = float(input())

        sum += grade
        total_score += grade
        counter += 1

    avg_score = sum / n

    print(f"{command} - {avg_score:.2f}.")

    command = input()

print(f"Student's final assessment is {(total_score / counter):.2f}.")
