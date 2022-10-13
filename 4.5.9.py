n = int(input())
matrix = [list(map(int, input().split())) for i in range(n)]

mtx_cols, main_diag, secondary_diag, mtx_line = [], [], [], []
# collect lists
for i in range(n):
    row = []
    main_diag.append(matrix[i][i])
    secondary_diag.append(matrix[i][n - i - 1])
    for j in range(n):
        mtx_line.append(matrix[i][j])
        row.append(matrix[j][i])
    mtx_cols.append(row)
mtx_line.sort()
# check sequence
for i in range(len(mtx_line) - 1):
    if mtx_line[i] == mtx_line[i + 1] - 1 and mtx_line[i] > 0:
        flag = True
    else:
        flag = False
        break
# check sums
for i in range(n):
    if sum(matrix[i]) == sum(mtx_cols[i]) == sum(main_diag) == sum(secondary_diag) and len(
            set(mtx_line)) == n ** 2 and flag:
        continue
    else:
        print('NO')
        break
else:
    print('YES')
# lst = map(int, open(0).read().split())
# print(lst)
