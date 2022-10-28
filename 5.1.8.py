n = int(input())
mtx = [[0] * n for j in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            mtx[i][j] = 0
        else:
            mtx[i][j] = abs(i - j)

[print(*i) for i in mtx]
