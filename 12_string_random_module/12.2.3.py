from random import shuffle

matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]
shuffle(matrix)
print(matrix)

# либо
# from random import shuffle
# matrix = [[1, 2, 3, 4],
#           [5, 6, 7, 8],
#           [9, 10, 11, 12],
#           [13, 14, 15, 16]]
# shuffle(matrix)
# [shuffle(i) for i in matrix]

# Напишите программу, которая с помощью модуля random перемешивает случайным образом содержимое матрицы (двумерного списка).
