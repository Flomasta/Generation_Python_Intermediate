n = int(input())
mtx = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        if j == n - i - 1:
            mtx[i][j] = 1
        elif i > n - 1 - j:
            mtx[i][j] = 2

[print(*i) for i in mtx]
