numbers = list(map(float, input().split()))

def solve(data):
    return [round(x) for x in data]

print(solve(numbers))
