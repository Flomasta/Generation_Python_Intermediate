n, m = int(input()), int(input())
matrix = [list(map(int, input().split())) for i in range(n)]
a, b = list(map(int, input().split()))
for i in range(n):
    matrix[i][a], matrix[i][b] = matrix[i][b], matrix[i][a]
[print(*i) for i in matrix]
