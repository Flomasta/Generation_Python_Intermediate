n, m = map(int, input().split())
mtx = []
lst = [i for i in range(1, n * m + 1)]

for i in range(n):
    if i % 2 == 0:
        mtx.append(lst[i * m:(i + 1) * m])
    else:
        mtx.append(lst[(i + 1) * m - 1:i * m - 1:-1])
[print(*i) for i in mtx]
