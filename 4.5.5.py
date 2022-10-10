n = int(input())
matrix = [list(map(int, input().split())) for i in range(n)]
for i in range(n):
    matrix[i][i], matrix[len(matrix) - i - 1][i] = matrix[len(matrix) - i - 1][i], matrix[i][i]

[print(*i) for i in matrix]
