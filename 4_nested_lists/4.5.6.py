m = n = int(input())
matrix = [list(map(int, input().split())) for i in range(n)]
if n % 2 != 0:
    m = n - 1
for i in range(int(m / 2)):
    for j in range(n):
        matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j]
[print(*i) for i in matrix]

# простое решение
# matrix.reverse() или [print(*r) for r in matrix[::-1]]

# Зеркальное отображение
# Дана квадратная матрица чисел. Напишите программу, которая зеркально отображает её элементы относительно горизонтальной оси симметрии.
#
# Формат входных данных
# На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы построчно через пробел.
#
# Формат выходных данных
# Программа должна вывести матрицу в которой зеркально отображены элементы относительно горизонтальной оси симметрии.
#
# Тестовые данные 🟢
# Sample Input 1:
#
# 4
# 1 2 3 4
# 5 6 7 8
# 8 6 4 2
# 3 4 5 6
# Sample Output 1:
#
# 3 4 5 6
# 8 6 4 2
# 5 6 7 8
# 1 2 3 4
# Sample Input 2:
#
# 3
# 1 2 3
# 4 5 6
# 7 8 9
# Sample Output 2:
#
# 7 8 9
# 4 5 6
# 1 2 3
# Sample Input 3:
#
# 2
# 1 1
# 1 1
# Sample Output 3:
#
# 1 1
# 1 1
