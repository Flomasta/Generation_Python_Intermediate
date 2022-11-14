n = int(input())
matrix = [list(map(int, input().split())) for i in range(n)]
max_num = []
for i in range(n):
    for j in range(n):
        if i > j or i == j:
            max_num.append(matrix[i][j])
print(max(max_num))

#вариант
# n=int(input())
# matrix=[[int(i) for i in input().split()] for _ in range(n)]
# print(max(max(matrix[i][j] for j in range(i+1)) for i in range(n)))


#вариант 2
# n = int(input())
# matrix = [[int(num) for num in input().split()] for i in range(n)]
# print(max(matrix[i][j] for i in range(n) for j in range(n) if i >= j))


# Максимальный в области 1
# Напишите программу, которая выводит максимальный элемент в заштрихованной области квадратной матрицы.
#
# Угол слева от основной диагогали  |\
#
# Формат входных данных
# На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы (целые числа) построчно через пробел.
#
# Формат выходных данных
# Программа должна вывести одно число — максимальный элемент в заштрихованной области квадратной матрицы.
#
# Примечание. Элементы главной диагонали также учитываются.
