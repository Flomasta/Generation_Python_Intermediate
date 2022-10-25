n, m = list(map(int, input().split()))
mtx_1 = [list(map(int, input().split())) for i in range(n)]
input()
mtx_2 = [list(map(int, input().split())) for i in range(n)]
mtx_sum = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        mtx_sum[i][j] = mtx_1[i][j] + mtx_2[i][j]

[print(*i) for i in mtx_sum]


# Сложение матриц
# Напишите программу для вычисления суммы двух матриц.
#
# Формат входных данных
# На вход программе подаются два натуральных числа nn и mm — количество строк и столбцов в матрицах, затем элементы первой матрицы, затем пустая строка, далее следуют элементы второй матрицы.
#
# Формат выходных данных
# Программа должна вывести результирующую матрицу, разделяя элементы символом пробела.
#
# Тестовые данные 🟢
# Sample Input 1:
#
# 2 4
# 1 2 3 4
# 5 6 7 1
#
# 3 2 1 2
# 1 3 1 3
# Sample Output 1:
#
# 4 4 4 6
# 6 9 8 4
# Sample Input 2:
#
# 3 3
# 9 6 3
# 3 1 1
# 4 7 5
#
# 0 3 2
# 1 7 8
# 4 2 3
# Sample Output 2:
#
# 9 9 5
# 4 8 9
# 8 9 8
# Sample Input 3:
#
# 1 1
# 1
#
# 1
# Sample Output 3:
#
# 2
