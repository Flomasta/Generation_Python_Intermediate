n = int(input())
matrix = [list(map(int, input().split())) for i in range(n)]
max_num = []
for i in range(n):
    for j in range(n):
        if i > j or i == j:
            max_num.append(matrix[i][j])
print(max(max_num))
