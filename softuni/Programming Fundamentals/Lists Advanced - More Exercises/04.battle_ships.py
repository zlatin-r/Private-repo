n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
targets = input().split()

destroyed = 0

for t in targets:
    row, col = tuple(map(int, t.split("-")))

    if matrix[row][col] > 0:
        matrix[row][col] -= 1

        if matrix[row][col] == 0:
            destroyed += 1

print(destroyed)
