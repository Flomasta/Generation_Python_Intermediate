# import numpy as np
#
# a, b = list(map(int, input().split()))
# mtx_1 = [list(map(int, input().split())) for i in range(a)]
# input()
# c, d = list(map(int, input().split()))
# mtx_2 = [list(map(int, input().split())) for i in range(c)]
#
# total = np.dot(mtx_1, mtx_2)
# [print(*i) for i in total]


a, b = list(map(int, input().split()))
mtx_1 = [list(map(int, input().split())) for i in range(a)]
input()
c, d = list(map(int, input().split()))
mtx_2 = [list(map(int, input().split())) for i in range(c)]
mtx_3 = [[0] * d for _ in range(a)]

for i in range(a):
    for j in range(d):
        for q in range(c):
            mtx_3[i][j] += mtx_1[i][q] * mtx_2[q][j]
[print(*i) for i in mtx_3]
