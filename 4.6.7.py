n, m = map(int, input().split())
mtx = [[0] * m for i in range(n)]

for i in range(n):
    for j in range(n):
        mtx[i][j] = (i + j) % m + 1

[print(*i) for i in mtx]
