init_list = list(map(int, input().split()))

command = input()

while command != "end":
    action = command.split(" ")[0]
    result = None

    if action == "exchange":
        index = int(command.split()[1])

        if 0 > index > len(init_list):
            result = "Invalid index"

        lst1 = init_list[:index +1]
        lst2 = init_list[index + 1:]
        init_list = lst2 + lst1

    elif action == "max":
        sub_command = command.split()[1]

        if sub_command == "odd":
            max_odd_num = max([x for x in init_list if x % 2 != 0])
            result = init_list.index(max_odd_num)
        elif sub_command == "even":
            max_even_num = max([x for x in init_list if x % 2 == 0])
            result = init_list.index(max_even_num)

        print(result)

    elif action == "min":
        sub_command = command.split()[1]

        if sub_command == "odd":
            try:
                min_odd_num = min([x for x in init_list if x % 2 != 0])
                result = init_list.index(min_odd_num)
            except ValueError:
                result = "No matches"
        elif sub_command == "even":
            try:
                min_even_num = min([x for x in init_list if x % 2 == 0])
                result = init_list.index(min_even_num)
            except ValueError:
                result = "No matches"

        print(result)

    elif action == "first":
        _, count, sub_command = command.split()
        count = int(count)
        result = []
        
        if sub_command == "even":
            for num in init_list:
                if num % 2 == 0 and num < count:
                    result.append(num)

        elif sub_command == "odd":
            for num in init_list:
                if num % 2 != 0 and len(result) < count:
                    result.append(num)

        print(result)

    elif action == "last":
        _, count, sub_command = command.split()
        count = int(count)
        result = []

        if count > len(init_list):
            result = "Invalid count"
            break
        
        if sub_command == "even":
            for i in range(len(init_list) -1, -1, -1):
                if init_list[i] % 2 == 0 and  len(result) < count:
                    result.append(init_list[i])

        elif sub_command == "odd":
            for i in range(len(init_list), -1, -1):
                if init_list[i] % 2 != 0 and  len(result) < count:
                    result.append(init_list[i])

        print(result)

    command = input()

print(init_list)
