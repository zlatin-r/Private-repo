from math import pi

figure = input()
result = 0

if figure == "square":
    a = float(input())
    result = a * a
elif figure == "rectangle":
    a = float(input())
    b = float(input())
    result = a * b
elif figure == "circle":
    r = float(input())
    result = pi * r ** 2
elif figure == "triangle":
    a = float(input())
    h = float(input())
    result = 0.5 * a * h

print(f"{result:.3f}")
