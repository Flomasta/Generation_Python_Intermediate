from decimal import *

num = Decimal(input().replace('-', ''))
a = tuple(num.as_tuple().digits)
if str(num).startswith('0'):
    a += (0,)
print(a)
print(max(a) + min(a))


#отличное решение
# from decimal import *
# num = Decimal(input())
# cyphers = num.as_tuple().digits
# print(max(cyphers) + min(cyphers) * (abs(num) >= 1))


#вариант
# from decimal import *
# num = list(input())
# a = [abs(int(i)) for i in num if i in '0123456789']
# print(min(a) + max(a))


# Дополните приведенный код, чтобы он вывел сумму наибольшей и наименьшей цифры Decimal числа.
