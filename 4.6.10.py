n, m = map(int, input().split())
mtx = [[0] * m for i in range(n)]

counter = 1
x, y = 0, -1
d_row = 0
d_col = 1
while counter <= n * m:
    if 0 <= x + d_row < n and 0 <= y + d_col < m and mtx[x + d_row][y + d_col] == 0:
        x += d_row
        y += d_col
        mtx[x][y] = counter
        counter += 1
    else:
        if d_col == 1:
            d_col = 0
            d_row = 1
        elif d_row == 1:
            d_row = 0
            d_col = -1
        elif d_col == -1:
            d_col = 0
            d_row = -1
        elif d_row == -1:
            d_row = 0
            d_col = 1
[print(*i) for i in mtx]

#делении любых чисел по модулю на размер матрицы координаты не выходят за пределы массива
# вариант решения:
# n, m = map(int, input().split())
# a = [[0] * m for _ in range(n)]
# dr, dc, r, c = 0, 1, 0, 0
#
# for cnt in range(1, n * m + 1):
#     a[r][c] = cnt
#
#     if a[(r + dr) % n][(c + dc) % m]:
#         dr, dc = dc, -dr
#
#     r += dr
#     c += dc
#
# for row in a:
#     print(*(f'{e:<3}' for e in row), sep='')
#
# Заполнение спиралью 😈😈
# На вход программе подаются два натуральных числа nn и mm. Напишите программу, которая создает матрицу размером n \times mn×m заполнив её "спиралью" в соответствии с образцом.
#
# Формат входных данных
# На вход программе на одной строке подаются два натуральных числа nn и mm — количество строк и столбцов в матрице.
#
# Формат выходных данных
# Программа должна вывести матрицу в соответствии образцом.
#
# Примечание. Для вывода элементов матрицы как в примерах, отводите ровно 33 символа на каждый элемент. Для этого используйте строковый метод ljust(). Можно обойтись и без ljust(), система примет и такое решение 😇
#
# Тестовые данные 🟢
# Sample Input 1:
#
# 4 5
# Sample Output 1:
#
# 1  2  3  4  5
# 14 15 16 17 6
# 13 20 19 18 7
# 12 11 10 9  8
# Sample Input 2:
#
# 1 6
# Sample Output 2:
#
# 1  2  3  4  5  6
# Sample Input 3:
#
# 3 3
# Sample Output 3:
#
# 1  2  3
# 8  9  4
# 7  6  5
