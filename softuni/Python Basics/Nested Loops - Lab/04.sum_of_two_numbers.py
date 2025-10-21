start = int(input())
end = int(input())
magic_num = int(input())

counter = 0
found = False
result = ""

for x in range(start, end + 1):
    for y in range(start, end + 1):
        counter += 1

        if x + y == magic_num:
            if not found:
                result = f"Combination N:{counter} ({x} + {y} = {magic_num})"
                found = True

if not found:
    print(f"{counter} combinations - neither equals {magic_num}")
else:
    print(result)
