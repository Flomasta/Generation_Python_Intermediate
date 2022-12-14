# import numpy as np
#
# a, b = list(map(int, input().split()))
# mtx_1 = [list(map(int, input().split())) for i in range(a)]
# input()
# c, d = list(map(int, input().split()))
# mtx_2 = [list(map(int, input().split())) for i in range(c)]
#
# total = np.dot(mtx_1, mtx_2)
# [print(*i) for i in total]


a, b = list(map(int, input().split()))
mtx_1 = [list(map(int, input().split())) for i in range(a)]
input()
c, d = list(map(int, input().split()))
mtx_2 = [list(map(int, input().split())) for i in range(c)]
mtx_3 = [[0] * d for _ in range(a)]

for i in range(a):
    for j in range(d):
        for q in range(c):
            mtx_3[i][j] += mtx_1[i][q] * mtx_2[q][j]
[print(*i) for i in mtx_3]


# Умножение матриц 🌶️
# Напишите программу, которая перемножает две матрицы.
#
# Формат входных данных
# На вход программе подаются два натуральных числа nn и mm — количество строк и столбцов в первой матрице, затем элементы первой матрицы, затем пустая строка. Далее следуют числа mm и kk — количество строк и столбцов второй матрицы затем элементы второй матрицы.
#
# Формат выходных данных
# Программа должна вывести результирующую матрицу, разделяя элементы символом пробела.
#
# Тестовые данные 🟢
# Sample Input 1:
#
# 2 2
# 1 2
# 3 2
#
# 2 2
# 3 2
# 1 1
# Sample Output 1:
#
# 5 4
# 11 8
# Sample Input 2:
#
# 3 2
# 2 5
# 6 7
# 1 8
#
# 2 3
# 1 2 1
# 0 1 0
# Sample Output 2:
#
# 2 9 2
# 6 19 6
# 1 10 1
# Sample Input 3:
#
# 3 3
# 2 4 6
# 1 3 5
# 0 4 8
#
# 3 3
# 6 3 1
# 9 6 3
# 0 2 0
# Sample Output 3:
#
# 48 42 14
# 33 31 10
# 36 40 12
