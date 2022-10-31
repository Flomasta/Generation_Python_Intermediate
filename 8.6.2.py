n, m = [set(map(int, input().split())) for i in range(2)]
s = n & m
print(*sorted(list(s)))


# Общие числа
# На вход программе подаются две строки текста, содержащие числа. Напишите программу, которая выводит все числа в порядке возрастания, которые есть как в первой строке, так и во второй.
#
# Формат входных данных
# На вход программе подаются две строки текста, содержащие числа, отделенные символом пробела.
#
# Формат выходных данных
# Программа должна вывести множество чисел, встречающихся в обеих строках.
#
# Тестовые данные 🟢
# Sample Input 1:
#
# 1 2 3
# 1 2 4 5
# Sample Output 1:
#
# 1 2
# Sample Input 2:
#
# 1 3 5
# 5 3 1
# Sample Output 2:
#
# 1 3 5
# Sample Input 3:
#
# 1 7 8 9 7 3
# 6 4 3 2 7 3 10 5
# Sample Output 3:
#
# 3 7