electrons = int(input())

filled_shells = []
remaining = electrons
n = 1

while remaining > 0:
    capacity = 2 * n**2
    filled_shells.append(min(capacity, remaining))
    remaining -= min(capacity, remaining)
    n += 1

print(filled_shells)
