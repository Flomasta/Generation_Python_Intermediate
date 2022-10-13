n = int(input())
mtx = [[0] * n for i in range(n)]

for i in range(n):
    for j in range(n):
        if (i <= j and i <= n - 1 - j) or (i >= j and i >= n - 1 - j):
            mtx[i][j] = 1
[print(*i) for i in mtx]
