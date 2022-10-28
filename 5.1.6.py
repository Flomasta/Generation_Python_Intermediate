n = int(input())
mtx = [list(map(int, input().split())) for j in range(n)]
mask = [i for i in range(1, n + 1)]
flag = False

for i in mtx:
    if set(mask) != set(i):
        break
else:
    for i in zip(*mtx):
        if set(mask) != set(i):
            break
    else:
        flag = True
print('YES' if flag else 'NO')

# решение при помощи sorted
# n = int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# numbers = list(range(1, n + 1))
# result = 'YES'
#
# for i in range(n):
#     row_nums = sorted(matrix[i])
#     col_nums = sorted([matrix[j][i] for j in range(n)])
#     if row_nums != numbers or col_nums != numbers:
#         result = 'NO'
#         break
#
# print(result)

# Латинский квадрат 🌶️
# Латинским квадратом порядка nn называется квадратная матрица размером n \times nn×n, каждая строка и каждый столбец которой содержат все числа от 11 до nn. Напишите программу, которая проверяет, является ли заданная квадратная матрица латинским квадратом.
#
# Формат входных данных
# На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы: nn строк, по nn чисел в каждой, разделённые пробелами.
#
# Формат выходных данных
# Программа должна вывести слово YES, если матрица является латинским квадратом, и слово NO, если не является.
#
# Тестовые данные 🟢
# Sample Input 1:
#
# 4
# 2 3 4 1
# 3 4 1 2
# 4 1 2 3
# 1 2 3 4
# Sample Output 1:
#
# YES
# Sample Input 2:
#
# 3
# 1 2 3
# 3 2 1
# 2 3 4
# Sample Output 2:
#
# NO
