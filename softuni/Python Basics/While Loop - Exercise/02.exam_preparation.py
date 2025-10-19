fail_grades = int(input())
total_score = 0
curr_fails = 0
tasks_count = 0
last_task = ""

while True:
    task_name = input()
  
    if task_name == "Enough":
        print(f"Average score: {(total_score / tasks_count):.2f}")
        print(f"Number of problems: {tasks_count}")
        print(f"Last problem: {last_task}")
        break

    grade = int(input())

    if grade <= 4:
        curr_fails += 1

        if curr_fails == fail_grades:
            print(f"You need a break, {curr_fails} poor grades.")
            break
    
    last_task = task_name
    total_score += grade
    tasks_count += 1
    