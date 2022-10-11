m = n = int(input())
matrix = [list(map(int, input().split())) for i in range(n)]
if n % 2 != 0:
    m = n - 1
for i in range(int(m / 2)):
    for j in range(n):
        matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j]
[print(*i) for i in matrix]
