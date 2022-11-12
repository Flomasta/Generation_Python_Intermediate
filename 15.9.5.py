a, b = int(input()), int(input())

def checker(item):
    return all([int(i) != 0 and item % int(i) == 0 for i in list(str(item))])

print(*list(filter(checker, range(a, b))))

# Интересные числа
# На вход программе подаются два натуральных числа aa и bb. Напишите программу с использованием встроенной функции all() для обнаружения всех целых чисел в диапазоне [a; \, b][a;b], которые делятся на каждую содержащуюся в них цифру без остатка.
#
# Формат входных данных
# На вход программе подаются два натуральных числа aa и bb на отдельных строках.
#
# Формат выходных данных
# Программа должна вывести все числа из диапазона [a; \, b][a;b], удовлетворяющие условию задачи, на одной строке, разделяя их символом пробела.
#
# Примечание. Числа, содержащие нули, неинтересны, их выводить не нужно.
#
# Тестовые данные 🟢
# Sample Input 1:
#
# 1
# 25
# Sample Output 1:
#
# 1 2 3 4 5 6 7 8 9 11 12 15 22 24
# Sample Input 2:
#
# 20
# 30
# Sample Output 2:
#
# 22 24
# Sample Input 3:
#
# 50
# 150
# Sample Output 3:
#
# 55 66 77 88 99 111 112 115 122 124 126 128 132 135 144