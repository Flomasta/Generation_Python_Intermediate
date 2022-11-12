with open('population.txt', 'r', encoding='utf-8') as file:
    data = list(map(lambda x: x.strip().split('\t'), file.readlines()))


    def checker(item):
        return ord(item[0][0]) == 71 and int(item[1]) > 500_000


    res = filter(checker, data)
    [print(i[0]) for i in res]

# Необычные страны
# Вам доступен текстовый файл population.txt с названиями стран и численностью их населения, разделенными символом табуляции '\t'.
#
# Напишите программу выводящую все страны, название которых начинается с буквы 'G', численность населения которых больше чем 500 \, 000500000 человек, не меняя их порядок.
#
# Формат входных данных
# На вход программе ничего не подается.
#
# Формат выходных данных
# Программа должна вывести названия стран, удовлетворяющие условиям задачи, каждое на отдельное строке.
#
# Примечание. Указанный файл можно скачать по ссылке.