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


# Напишите программу, которая выводит максимальный элемент в заштрихованной области квадратной матрицы.
#______
# |><|
#______
# Формат входных данных
# На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы (целые числа) построчно через пробел.
#
# Формат выходных данных
# Программа должна вывести одно число — максимальный элемент в заштрихованной области квадратной матрицы.
