matrix = [list(map(int, input().split())) for i in range(int(input()))]

for i in range(len(matrix)):
    res = []
    for j in range(len(matrix)):
        if matrix[i][j] > sum(matrix[i]) / len(matrix):
            res.append(1)
    print(sum(res))

 # Вариант решения
# for _ in range(int(input())):
#     lst = list(map(int, input().split()))
#     avg = sum(lst) / len(lst)
#     print(sum(i > avg for i in lst))


# Больше среднего
# Напишите программу, которая выводит количество элементов квадратной матрицы в каждой строке, больших среднего арифметического элементов данной строки.
#
# Формат входных данных
# На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы (целые числа) построчно через пробел.
#
# Формат выходных данных
# Программа должна вывести nn чисел — для каждой строки количество элементов матрицы, больших среднего арифметического элементов данной строки.
#
# Тестовые данные 🟢
# Sample Input 1:
#
# 4
# 1 2 3 4
# 5 6 3 15
# 0 2 3 1
# 5 2 8 5
# Sample Output 1:
#
# 2
# 1
# 2
# 1
# Sample Input 2:
#
# 2
# 5 6
# 99 5
# Sample Output 2:
#
# 1
# 1
# Sample Input 3:
#
# 3
# 666 666 666
# 777 777 777
# 100 100 100
# Sample Output 3:
#
# 0
# 0
# 0
