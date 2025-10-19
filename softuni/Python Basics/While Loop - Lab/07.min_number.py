command = input()
min_num = None

while command != "Stop":
    number = int(command)

    if min_num is None or number < min_num:
        min_num = number

    command = input()

print(min_num)
