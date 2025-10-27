numbers = list(map(int, input().split()))

def solve(data):
    min_num = min(data)
    max_num = max(data)
    sum_nums = sum(data)

    return f"The minimum number is {min_num}\nThe maximum number is {max_num}\nThe sum number is: {sum_nums}"

print(solve(numbers))
