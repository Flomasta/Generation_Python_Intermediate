n = int(input())
mtx = [list(map(int, input().split())) for j in range(n)]
max_num = mtx[0][n - 1]
for i in range(n):
    for j in range(n):
        if i >= n - 1 - j and max_num < mtx[i][j]:
            max_num = mtx[i][j]
print(max_num)

# альтернативное решение
#
# n = int(input())
# print(max(int(s) for i in range(n) for s in (input().split()[-1 - i:])))

# Максимальный в области 2
# Напишите программу, которая выводит максимальный элемент в заштрихованной области квадратной матрицы.
#
#
#
# Формат входных данных
# На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы.
#
# Формат выходных данных
# Программа должна вывести одно число — максимальный элемент в заштрихованной области квадратной матрицы.
#
# Примечание. Элементы побочной диагонали также учитываются.
#
# Тестовые данные 🟢
# Sample Input 1:
#
# 3
# 1 4 5
# 6 7 8
# 1 1 6
# Sample Output 1:
#
# 8
# Sample Input 2:
#
# 4
# 0 1 4 6
# 0 0 2 5
# 0 0 0 7
# 0 0 0 0
# Sample Output 2:
#
# 7
# Sample Input 3:
#
# 2
# 6 0
# 7 9
# Sample Output 3:
#
# 9
