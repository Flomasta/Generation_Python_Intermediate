d = {}
for _ in range(int(input())):
    v, *k = input().split()
    d[tuple(k)] = v

lst = [input() for i in range(int(input()))]

for i in lst:
    for k, v in d.items():
        if i in k:
            print(v)

# очень хорошее решение

# d = {}
# for _ in range(int(input())):
#     country, *cities = input().split()
#     d.update(dict.fromkeys(cities, country))
# for _ in range(int(input())):
#     print(d[input()])


#
# Страны и города
# На вход программе подается список стран и городов каждой страны. Затем даны названия городов. Напишите программу, которая для каждого города выводит, в какой стране он находится.
#
# Формат входных данных
# Программа получает на вход количество стран nn. Далее идет nn строк, каждая строка начинается с названия страны, затем идут названия городов этой страны. В следующей строке записано число mm, далее идут mm запросов — названия каких-то mm городов, из перечисленных выше.
#
# Формат выходных данных
# Программа должна вывести название страны, в которой находится данный город в соответствии с примером.
#
# Тестовые данные 🟢
# Sample Input:
#
# 2
# Германия Берлин Мюнхен Гамбург Дортмунд
# Нидерланды Амстердам Гаага Роттердам Алкмар
# 4
# Амстердам
# Алкмар
# Гамбург
# Гаага
# Sample Output:
#
# Нидерланды
# Нидерланды
# Германия
# Нидерланды
