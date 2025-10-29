def anonymous_threat():
    data = input().split()

    while True:
        command = input()
        if command == "3:1":
            break

        tokens = command.split()
        action = tokens[0]

        if action == "merge":
            start_index = int(tokens[1])
            end_index = int(tokens[2])

            start_index = max(0, start_index)
            end_index = min(len(data) - 1, end_index)

            if start_index < end_index:
                merged = ''.join(data[start_index:end_index + 1])
                data[start_index:end_index + 1] = [merged]

        elif action == "divide":
            index = int(tokens[1])
            partitions = int(tokens[2])
            element = data[index]

            if partitions > 0:
                part_length = len(element) // partitions
                divided = []

                for i in range(partitions):
                    if i == partitions - 1:
                        divided.append(element[i * part_length:])
                    else:
                        divided.append(element[i * part_length:(i + 1) * part_length])

                data[index:index + 1] = divided

    print(' '.join(data))


anonymous_threat()
