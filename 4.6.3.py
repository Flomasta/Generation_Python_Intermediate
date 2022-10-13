n, m = list(map(int, input().split()))
mtx = [[0] * m for i in range(n)]
counter = 1
for i in range(n):
    for j in range(m):
        mtx[i][j] = counter
        counter += 1
[print(*i) for i in mtx]
