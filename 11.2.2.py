txt = input().split()

print([txt[:i + 1].count(txt[i]) for i in range(len(txt))])

#
# решение через словарь:
#
# s = input().split()
# d = {}
# for i in s:
#     d[i] = d.get(i, 0) + 1
#     print(d[i], end = ' ')


# Порядковый номер
# Дана строка текста на русском языке, состоящая из слов и символов пробела. Словом считается последовательность букв, слова разделены одним пробелом или несколькими.
#
# Напишите программу, определяющую для каждого слова порядковый номер его вхождения в текст именно в этой форме, с учетом регистра. Для первого вхождения слова программа выведет 11, для второго вхождения того же слова — 22 и т. д.
#
# Формат входных данных
# Программа получает на вход единственную строку текста, состоящую только из русских букв и символов пробела.
#
# Формат выходных данных
# Для каждого слова исходного текста программа выводит одно целое число — номер вхождения этого слова в текст. Числа необходимо вывести на одной строке через пробел.
#
# Примечание. Количество чисел должно совпадать с количеством слов исходного текста.
#
# Тестовые данные 🟢
# Sample Input 1:
#
# прием Хьюстон Хьюстон как слышно прием меня слышно прием хьюстон
# Sample Output 1:
#
# 1 1 2 1 1 2 1 2 3 1
# Sample Input 2:
#
# Привет что делаешь что нового что с работой как там с деньгами
# Sample Output 2:
#
# 1 1 1 2 1 3 1 1 1 1 2 1
