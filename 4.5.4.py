# put your python code here
n = int(input())
matrix = [list(map(int, input().split())) for i in range(n)]
flag = True
for i in range(n):
    for j in range(n):
        if i > j and i != j and matrix[i][j] != matrix[j][i]:
            print('NO')
            break
    else:
        continue
    break
else:
    print('YES')
