n, m = map(int, input().split())
mtx = [[0] * m for i in range(n)]

for i in range(n):
    for j in range(m):
        mtx[i][j] = i + 1 + n * j
[print(*i) for i in mtx]
