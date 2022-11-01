n, m = set(input().split()), set(input().split())
print('YES' if n == m else 'NO')

# Онлайн-школа BEEGEEK 1
# При приёме новых сотрудников в онлайн-школу BEEGEEK её руководитель тестирует не только профессиональные качества кандидата, но и его память.
#
# Кандидату показывают ненадолго несколько различных чисел, а затем кандидат должен их назвать. Причем неважно, в каком порядке он их вспоминает, и повторяется он или нет, главное он должен назвать все числа, не добавляя лишних.
#
# Напишите программу, определяющую, успешно ли прошел кандидат тестирование памяти.
#
# Формат входных данных
# На вход программе подаются две строки с числами: в первой строке показанные кандидату, а во второй ответы кандидата.
#
# Формат выходных данных
# Программа должна вывести YES, если кандидат прошел испытание и его можно брать на работу и NO в противном случае.
#
# Тестовые данные 🟢
# Sample Input 1:
#
# 8
# 9
# Sample Output 1:
#
# NO
# Sample Input 2:
#
# 1 2 3 4 8 5
# 1 2 8 2 3 4 5 2
# Sample Output 2:
#
# YES
# Sample Input 3:
#
# 14 64 34 34 34 34 87 100
# 100 14 64 34 100
# Sample Output 3:
#
# NO
