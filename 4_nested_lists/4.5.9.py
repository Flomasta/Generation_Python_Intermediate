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

# отличное решение
# n = int(input())
# a = [[*map(int, input().split())] for _ in range(n)]
# print(('NO', 'YES')[set(sum(a, [])) == set((*range(1, n ** 2 + 1),))   # ряд натур. чисел до n ** 2
#                     and
#                     len(set(map(sum, (*a,                              # суммы строк
#                                       *zip(*a),                            # суммы столбцов (транспон-ый кв-т)
#                                       [a[i][i] for i in range(n)],         # сумма гл. диагоналей
#                                       [a[i][~i] for i in range(n)]))       # сумма втор. диагонали
#                             )) == 1])                                       # все они должны совпадать




# Магический квадрат 🌶️
# Магическим квадратом порядка nn называется квадратная таблица размера n \times nn×n, составленная из всех чисел 1, 2, 3, \ldots, n^21,2,3,…,n
# 2
# так, что суммы по каждому столбцу, каждой строке и каждой из двух диагоналей равны между собой. Напишите программу, которая проверяет, является ли заданная квадратная матрица магическим квадратом.
#
# Формат входных данных
# На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы: nn строк, по nn чисел в каждой, разделённые пробелами.
#
# Формат выходных данных
# Программа должна вывести слово YES, если матрица является магическим квадратом, и слово NO в противном случае.
#
# Тестовые данные 🟢
# Sample Input 1:
#
# 3
# 8 1 6
# 3 5 7
# 4 9 2
# Sample Output 1:
#
# YES
# Sample Input 2:
#
# 3
# 8 2 6
# 3 5 7
# 4 9 1
# Sample Output 2:
#
# NO
# Sample Input 3:
#
# 3
# 4 9 2
# 3 5 7
# 8 1 6
# Sample Output 3:
#
# YES
