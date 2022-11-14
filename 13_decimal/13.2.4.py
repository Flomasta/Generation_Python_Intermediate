from fractions import Fraction

n, m = input(),input()
n_f, m_f = Fraction(n), Fraction(m)
print(f'{n} + {m} = {n_f + m_f}')
print(f'{n} - {m} = {n_f - m_f}')
print(f'{n} * {m} = {n_f * m_f}')
print(f'{n} / {m} = {n_f / m_f}')


#вариант
# from fractions import Fraction
#
# x, y = input(), input()
# for op in '+-*/':
#     print(f'{x} {op} {y} = {eval(f"Fraction(x){op}Fraction(y)")}')


# Операции над дробями
# Даны две дроби в формате a/b. Напишите программу, которая вычисляет и выводит их сумму, разность, произведение и частное.
#
# Формат входных данных
# На вход программе подаются две ненулевые дроби, каждая на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести сумму, разность, произведение и частное двух дробей.
#
# Примечание. Обратите внимание на третий тест: исходные дроби сокращать не нужно, а результат нужно.
#
# Тестовые данные 🟢
# Sample Input 1:
#
# 2/3
# 3/7
# Sample Output 1:
#
# 2/3 + 3/7 = 23/21
# 2/3 - 3/7 = 5/21
# 2/3 * 3/7 = 2/7
# 2/3 / 3/7 = 14/9
# Sample Input 2:
#
# 3/4
# 1/4
# Sample Output 2:
#
# 3/4 + 1/4 = 1
# 3/4 - 1/4 = 1/2
# 3/4 * 1/4 = 3/16
# 3/4 / 1/4 = 3
# Sample Input 3:
#
# 5/10
# 10/5
# Sample Output 3:
#
# 5/10 + 10/5 = 5/2
# 5/10 - 10/5 = -3/2
# 5/10 * 10/5 = 1
# 5/10 / 10/5 = 1/4