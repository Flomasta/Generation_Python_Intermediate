n, m = list(map(int, input().split()))

for i in range(n):
    mtx = [['.*'[(i + j) % 2 != 0] for j in range(m)] for i in range(n)]
[print(*i) for i in mtx]
