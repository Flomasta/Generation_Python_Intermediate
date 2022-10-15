n, m = map(int, input().split())
mtx = [[0] * m for i in range(n)]

diag = n + m + 1
counter = 1
for col in range(diag):
    for i in range(n):
        for j in range(m):
            if col == i + j:
                mtx[i][j] = counter
                counter += 1
[print(*i) for i in mtx]
