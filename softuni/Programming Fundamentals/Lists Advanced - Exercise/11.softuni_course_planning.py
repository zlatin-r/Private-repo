def course_planning():
    schedule = input().split(", ")

    while True:
        command = input()
        if command == "course start":
            break

        parts = command.split(":")
        action = parts[0]
        lesson = parts[1]

        if action == "Add":
            if lesson not in schedule:
                schedule.append(lesson)

        elif action == "Insert":
            index = int(parts[2])
            if lesson not in schedule:
                schedule.insert(index, lesson)

        elif action == "Remove":
            if lesson in schedule:
                schedule.remove(lesson)
            exercise = f"{lesson}-Exercise"
            if exercise in schedule:
                schedule.remove(exercise)

        elif action == "Swap":
            lesson2 = parts[2]
            if lesson in schedule and lesson2 in schedule:
                i1, i2 = schedule.index(lesson), schedule.index(lesson2)
                schedule[i1], schedule[i2] = schedule[i2], schedule[i1]

                # Handle exercises (move them along with their lessons)
                ex1, ex2 = f"{lesson}-Exercise", f"{lesson2}-Exercise"

                if ex1 in schedule:
                    schedule.remove(ex1)
                    schedule.insert(schedule.index(lesson) + 1, ex1)

                if ex2 in schedule:
                    schedule.remove(ex2)
                    schedule.insert(schedule.index(lesson2) + 1, ex2)

        elif action == "Exercise":
            exercise = f"{lesson}-Exercise"
            if lesson in schedule:
                if exercise not in schedule:
                    schedule.insert(schedule.index(lesson) + 1, exercise)
            else:
                schedule.append(lesson)
                schedule.append(exercise)

    # Print final schedule with numbering
    for i, lesson in enumerate(schedule, 1):
        print(f"{i}.{lesson}")


course_planning()
