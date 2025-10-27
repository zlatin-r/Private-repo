num_a = int(input())
num_b = int(input())
num_c = int(input())

def sum_numbers(a, b):
    return a + b

def subtract(func, c):
    return func - c

print(subtract(sum_numbers(num_a, num_b), num_c))
