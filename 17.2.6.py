with open('file.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    words = [len(i.split()) for i in lines]
    letters = [j.strip('.,;:-?!') for i in lines for j in i.split()]
    letters = len([letter for word in letters for letter in word if letter.isalpha()])

    print(f'''Input file contains:
{letters} letters 
{sum(words)} words 
{len(lines)} lines ''')
# Статистика по файлу
# Вам доступен текстовый файл file.txt, набранный латиницей. Напишите программу, которая выводит количество букв латинского алфавита, слов и строк. Выведите три найденных числа в формате, приведенном в примере.
#
# Формат входных данных
# На вход программе ничего не подается.
#
# Формат выходных данных
# Программа должна вывести три найденных числа в формате, приведенном в примере.
#
# Примечание 1. Если бы файл file.txt содержал строки:
#
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# то результатом было бы:
#
# Input file contains:
# 108 letters
# 20 words
# 4 lines
# Примечание 2. Словом называется последовательность из непробельных символов. Например, строка
#
# abc a21 67pop    qwert bo7ok 83456
# содержит 66 слов: abc, a21, 67pop, qwert, bo7ok, 83456.
#
# Примечание 3. Указанный файл можно скачать по ссылке.
