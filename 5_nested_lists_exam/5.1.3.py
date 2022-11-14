n = int(input())
mtx = [list(map(int, input().split())) for j in range(n)]

for i in range(n):
    for j in range(n):
        print(mtx[j][i], end=' ')
    print()


# Транспонирование матрицы
# Напишите программу, которая транспонирует квадратную матрицу.
#
# Формат входных данных
# На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы.
#
# Формат выходных данных
# Программа должна вывести транспонированную матрицу.
#
# Примечание 1. Транспонированная матрица — матрица, полученная из исходной матрицы заменой строк на столбцы.
#
# Примечание 2. Задачу можно решить без использования вспомогательного списка.
#
# Тестовые данные 🟢
# Sample Input 1:
#
# 3
# 1 2 3
# 4 5 6
# 7 8 9
# Sample Output 1:
#
# 1 4 7
# 2 5 8
# 3 6 9
# Sample Input 2:
#
# 4
# 1 2 3 1
# 4 5 6 4
# 7 8 9 7
# 1 2 3 8
# Sample Output 2:
#
# 1 4 7 1
# 2 5 8 2
# 3 6 9 3
# 1 4 7 8
# Sample Input 3:
#
# 2
# 5 6
# 8 4
# Sample Output 3:
#
# 5 8
# 6 4