n, m = list(map(int, input().split()))
mtx_1 = [list(map(int, input().split())) for i in range(n)]
input()
mtx_2 = [list(map(int, input().split())) for i in range(n)]
mtx_sum = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        mtx_sum[i][j] = mtx_1[i][j] + mtx_2[i][j]

[print(*i) for i in mtx_sum]
