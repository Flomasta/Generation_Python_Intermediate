import numpy as np

a, b = list(map(int, input().split()))
mtx_1 = [list(map(int, input().split())) for i in range(a)]
input()
c, d = list(map(int, input().split()))
mtx_2 = [list(map(int, input().split())) for i in range(c)]

total = np.dot(mtx_1, mtx_2)
[print(*i) for i in total]
