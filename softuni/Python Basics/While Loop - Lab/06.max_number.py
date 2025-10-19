command = input()
max_num = None

while command != "Stop":
    number = int(command)

    if max_num is None or number > max_num:
        max_num = number

    command = input()

print(max_num)
