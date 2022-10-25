n, m = map(int, input().split())
mtx = [[0] * m for i in range(n)]

diag = n + m + 1
counter = 1
for col in range(diag):
    for i in range(n):
        for j in range(m):
            if col == i + j:
                mtx[i][j] = counter
                counter += 1
[print(*i) for i in mtx]


# отличное решение
# n, m = [int(i) for i in input().split()]
#
# matrix = [[1] * m for _ in range(n)]
# row, col, diag = 0, 0, 0
#
# for i in range(1, n * m):
#     col -= 1
#     row += 1
#     if col < 0 or row == n:
#         diag += 1
#         col = diag if diag < m else m - 1
#         row = diag - col
#
#     matrix[row][col] += i
#
# [print(*i) for i in matrix]


# Заполнение диагоналями 🌶️
# На вход программе подаются два натуральных числа nn и mm. Напишите программу, которая создает матрицу размером n \times mn×m заполнив её "диагоналями" в соответствии с образцом.
#
# Формат входных данных
# На вход программе на одной строке подаются два натуральных числа nn и mm — количество строк и столбцов в матрице.
#
# Формат выходных данных
# Программа должна вывести указанную матрицу в соответствии с образцом.
#
# Примечание. Для вывода элементов матрицы как в примерах, отводите ровно 33 символа на каждый элемент. Для этого используйте строковый метод ljust(). Можно обойтись и без ljust(), система примет и такое решение 😇
#
# Тестовые данные 🟢
# Sample Input 1:
#
# 3 5
# Sample Output 1:
#
# 1  2  4  7  10
# 3  5  8  11 13
# 6  9  12 14 15
# Sample Input 2:
#
# 3 4
# Sample Output 2:
#
# 1  2  4  7
# 3  5  8  10
# 6  9  11 12
# Sample Input 3:
#
# 2 2
# Sample Output 3:
#
# 1  2
# 3  4
# Sample Input 4:
#
# 8 1
# Sample Output 4:
#
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# Sample Input 5:
#
# 8 2
# Sample Output 5:
#
# 1  2
# 3  4
# 5  6
# 7  8
# 9  10
# 11 12
# 13 14
# 15 16
