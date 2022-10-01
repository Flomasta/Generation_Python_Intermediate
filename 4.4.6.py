n = int(input())
matrix = [list(map(int, input().split())) for i in range(n)]
lst = []
for i in range(n):
    for j in range(n):
        a = matrix[i][j]
        if i < j and i < n - 1 - j or i > j and i > n - 1 - j:
            continue
        else:
            lst.append(matrix[i][j])
print(max(lst))
