# put your python code here
n = int(input())
matrix = [list(map(int, input().split())) for i in range(n)]
flag = True
for i in range(n):
    for j in range(n):
        if i > j and i != j and matrix[i][j] != matrix[j][i]:
            print('NO')
            break
    else:
        continue
    break
else:
    print('YES')


# хорошее решение
# n, a, ans = int(input()), [], 'YES'
# for i in range(n):
#     a.append(list(map(int, input().split())))
#     if any(a[i][j] != a[j][i] for j in range(i)):
#         ans = 'NO'
#         break
# print(ans)

#ещё одно решение
# n = int(input())
# matrix = [list(map(int, input().split())) for i in range(n)]
# if all([matrix[i][j] == matrix[j][i] for j in range(n) for i in range(n)]):
#     print('YES')
# else:
#     print('NO')
#


# Симметричная матрица
# Напишите программу, которая проверяет симметричность квадратной матрицы относительно главной диагонали.
#
# Формат входных данных
# На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы построчно через пробел.
#
# Формат выходных данных
# Программа должна вывести YES, если матрица симметрична относительно главной диагонали, и слово NO в противном случае.
#
# Тестовые данные 🟢
# Sample Input 1:
#
# 3
# 0 1 2
# 1 2 3
# 2 3 4
# Sample Output 1:
#
# YES
# Sample Input 2:
#
# 3
# 0 1 2
# 1 2 7
# 2 3 4
# Sample Output 2:
#
# NO
# Sample Input 3:
#
# 2
# 1 2
# 3 4
# Sample Output 3:
#
# NO
