from decimal import *

num = Decimal(input())
res = num.exp()+num.ln()+num.log10()+num.sqrt()
print(res)

# Математическое выражение
# На вход программе подается Decimal число dd. Напишите программу, которая вычисляет значение выражения:
# e^{d} + \ln(d) + \lg (d) + \sqrt{d}
# e
# d
# +ln(d)+lg(d)+
# d
# ​
#
#
# Формат входных данных
# На вход программе подается положительное десятичное число dd.
#
# Формат выходных данных
# Программа должна вывести искомое значение выражения.