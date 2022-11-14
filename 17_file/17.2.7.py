from random import choice

with open('../txt_files_for_part_files_and_files_exam/first_names.txt') as names, open(
        '../txt_files_for_part_files_and_files_exam/last_names.txt') as surnames:
    names = list(map(str.strip, names.readlines()))
    surnames = list(map(str.strip, surnames.readlines()))
    [print(choice(names), choice(surnames)) for _ in range(3)]

# Random name and surname
# Вам доступны два текстовых файла first_names.txt и last_names.txt, один с именами, другой с фамилиями.
#
# Напишите программу, которая c помощью модуля random создает 33 случайные пары имя + фамилия, а затем выводит их, каждую на отдельной строке.
#
# Формат входных данных
# На вход программе ничего не подается.
#
# Формат выходных данных
# Программа должна вывести текст в формате, приведенном в примере.
#
# Примечание 1. Если бы файлы first_names.txt и last_names.txt содержали строки:
#
# Aaron
# Abdul
# Abe
# Abel
# Abraham
# Albert
# и
#
# Abramson
# Adamson
# Adderiy
# Addington
# Adrian
# Albertson
# Einstein
# то результатом могло быть:
#
# Abdul Albertson
# Abel Adamson
# Albert Einstein
# Примечание 2. Указанные файлы можно скачать по ссылкам (имена, фамилии).
