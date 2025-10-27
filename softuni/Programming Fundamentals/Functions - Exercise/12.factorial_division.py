def factorial_division(a, b):

    fact_a = 1
    for i in range(1, a + 1):
        fact_a *= i

    fact_b = 1
    for i in range(1, b + 1):
        fact_b *= i

    result = fact_a / fact_b
    return f"{result:.2f}"

num1 = int(input())
num2 = int(input())

print(factorial_division(num1, num2))
