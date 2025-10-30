n = int(input())
matrix = [input().split() for _ in range(n)]

rows = n
cols = len(matrix[0])
visited = [[False]*cols for _ in range(rows)]
max_dots = 0

directions = [(-1,0),(1,0),(0,-1),(0,1)]

for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == '.' and not visited[i][j]:
            stack = [(i,j)]
            visited[i][j] = True
            count = 1

            while stack:
                r, c = stack.pop()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if matrix[nr][nc] == '.' and not visited[nr][nc]:
                            visited[nr][nc] = True
                            count += 1
                            stack.append((nr,nc))
            
            if count > max_dots:
                max_dots = count

print(max_dots)
