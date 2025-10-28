n = int(input())

free_chairs = 0
flag = True

for i in range(1, n + 1):
    chairs, visitors = input().split()

    count_chairs = len(chairs)
    visitors = int(visitors)

    if visitors > count_chairs:
        flag = False

        needed = visitors - count_chairs
        print(f"{needed} more chairs needed in room {i}")
    else:
        free_chairs += count_chairs - visitors

if flag:
    print(f"Game On, {free_chairs} free chairs left")
