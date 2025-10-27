from math import floor

def solve(a, b, c, d):
    position_a = abs(a) + abs(b)
    position_b = abs(c) + abs(d)

    if position_a < position_b:
        print(f"({floor(a)}, {floor(b)})")
    elif position_b < position_a:
        print(f"({floor(c)}, {floor(d)})")
    else:
        print(f"({floor(a)}, {floor(b)})")
        

ax = float(input())
ay = float(input())
bx = float(input())
by = float(input())

solve(ax, ay, bx, by)
