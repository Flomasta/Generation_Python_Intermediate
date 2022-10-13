n = int(input())
mtx = [[0] * n for i in range(n)]

for i in range(n):
    for j in range(n):
        if i == j or j == n - i - 1:
            mtx[i][j] = 1
[print(*i) for i in mtx]
