numbers = input().split(", ")

def solve(data):
    result = []

    for num in data:
        if num == num[::-1]:
            result.append("True")
        else:
            result.append("False")
                
    return "\n".join(result)

print(solve(numbers))
