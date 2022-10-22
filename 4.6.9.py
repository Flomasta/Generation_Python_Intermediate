n, m = map(int, input().split())
mtx = [[0] * m for i in range(n)]

diag = n + m + 1
counter = 1
for col in range(diag):
    for i in range(n):
        for j in range(m):
            if col == i + j:
                mtx[i][j] = counter
                counter += 1
[print(*i) for i in mtx]


# отличное решение
# n, m = [int(i) for i in input().split()]
#
# matrix = [[1] * m for _ in range(n)]
# row, col, diag = 0, 0, 0
#
# for i in range(1, n * m):
#     col -= 1
#     row += 1
#     if col < 0 or row == n:
#         diag += 1
#         col = diag if diag < m else m - 1
#         row = diag - col
#
#     matrix[row][col] += i
#
# [print(*i) for i in matrix]
