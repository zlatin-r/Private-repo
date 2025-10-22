people = int(input())
capacity = int(input())

courses = people // capacity
rest = people % capacity

if rest:
    courses += 1

print(courses)
