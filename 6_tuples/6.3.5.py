a, b, c = (int(input()) for i in range(3))

if a >0:
    x = - b / (2 * a)
    y = (4 * a * c - b ** 2) / (4 * a)
    print((x, y))

# Вершина параболы
# Уравнение параболы имеет вид y =ax^2 + bx + cy =ax
# 2
# +bx+c, где a \neq 0a
# 
# =0. Напишите программу, которая по введенным значениям a, b, ca,b,c определяет и выводит вершину параболы.
#
# Формат входных данных
# На вход программе подаются три целых числа, каждое на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести координаты вершины параболы.
#
# Примечание. Координаты вершины параболы y=ax^2+bx+cy=ax
# 2
# +bx+c имеют вид \left(-\dfrac{b}{2a}; \, \dfrac{4ac-b^2}{4a}\right)(−
#                                                                     2a
#                                                                     b
#                                                                     ​
#                                                                     ;
#                                                                     4a
#                                                                     4ac−b
#                                                                     2
#
#                                                                     ​
#                                                                     ).
#
# Тестовые данные 🟢
# Sample Input 1:
#
# -2
# 6
# 1
# Sample Output 1:
#
# (1.5, 5.5)
# Sample Input 2:
#
# -5
# 2
# 0
# Sample Output 2:
#
# (0.2, 0.2)
# Sample Input 3:
#
# 2
# 4
# -5
# Sample Output 3:
#
# (-1.0, -7.0)
