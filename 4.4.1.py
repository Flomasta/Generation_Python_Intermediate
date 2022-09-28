n, m = int(input()), int(input())
mtx = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(input())
    mtx.append(row)
[print(*mtx[i]) for i in range(len(mtx))]
