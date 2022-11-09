from fractions import Fraction

n = int(input())
st = set()
for i in range(n, 1, -1):
    for j in range(1, i):
        if int(Fraction(j, i)) == 0:
            st.add(Fraction(j, i))
print(*sorted(st), sep='\n')

# Упорядоченные дроби
# На вход программе подается натуральное число nn. Напишите программу, которая выводит в порядке возрастания все несократимые дроби, заключённые между 00 и 11, знаменатель которых не превосходит nn.
#
# Формат входных данных
# На вход программе подается натуральное число n, \, n > 1n,n>1.
#
# Формат выходных данных
# Программа должна вывести ответ на задачу.
#
# Примечание. Возможно вам потребуется функция gcd(), которая позволяет находить наибольший общий делитель (НОД) двух чисел. Функция реализована в модуле math.
#
# Тестовые данные 🟢
# Sample Input 1:
#
# 5
# Sample Output 1:
#
# 1/5
# 1/4
# 1/3
# 2/5
# 1/2
# 3/5
# 2/3
# 3/4
# 4/5
# Sample Input 2:
#
# 4
# Sample Output 2:
#
# 1/4
# 1/3
# 1/2
# 2/3
# 3/4
# Sample Input 3:
#
# 3
# Sample Output 3:
#
# 1/3
# 1/2
# 2/3
