n, m, k = set(map(int, input().split())), set(map(int, input().split())), set(map(int, input().split()))
marks = set(range(11))
res = marks - (n | m | k)
print(*sorted(res, key=int, reverse=True))

# Урок биологии
# Даны по 1010-балльной шкале оценки по биологии трех учеников. Напишите программу, которая выводит множество оценок, не встречающихся ни у одного из трех учеников.
#
# Формат входных данных
# На вход программе подаются оценки трех учеников, разделенные символом пробела (оценки каждого ученика на отдельной строке).
#
# Формат выходных данных
# Программа должна вывести множество оценок в порядке возрастания на одной строке, разделенных пробелами, в соответствии с условием задачи.
#
# Примечание. Оценка ученика находится в диапазоне от 00 до 1010 включительно.
#
# Тестовые данные 🟢
# Sample Input 1:
#
# 1 5 4 2 5 6 6 2 3 3 5 2
# 2 3 5 1 2 1 2 6 7 1 1 6
# 1 4 6 8 8 7 0 6 0 3 8 1
# Sample Output 1:
#
# 9 10
# Sample Input 2:
#
# 2 9 3 4 6 10
# 2 3 4 5 2 10
# 2 3 4 5 3 9
# Sample Output 2:
#
# 0 1 7 8
# Sample Input 3:
#
# 3 4 5 6 4 1 3 9 8 8
# 5 7 8 9 3 7 4 6 8 4
# 1 6 7 1 3 6 5 9 7 6
# Sample Output 3:
#
# 0 2 10
