n,m = set(input()),set(input())
print('YES' if n.isdisjoint(m) else 'NO')

# Одинаковые цифры
# На вход программе подаются два числа. Напишите программу, определяющую, есть ли в данных числах одинаковые цифры.
#
# Формат входных данных
# На вход программе подаются два натуральных числа, каждое на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести YES, если в записи данных чисел есть одинаковые цифры и NO если нет.
#
# Тестовые данные 🟢
# Sample Input 1:
#
# 114
# 223
# Sample Output 1:
#
# NO
# Sample Input 2:
#
# 1523
# 3678
# Sample Output 2:
#
# YES
# Sample Input 3:
#
# 5543
# 3455
# Sample Output 3:
#
# YES
