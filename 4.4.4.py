matrix = [list(map(int, input().split())) for i in range(int(input()))]

for i in range(len(matrix)):
    res = []
    for j in range(len(matrix)):
        if matrix[i][j] > sum(matrix[i]) / len(matrix):
            res.append(1)
    print(sum(res))
