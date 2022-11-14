from random import randrange

with open('../txt_files_for_part_files_and_files_exam/random.txt', 'a', encoding='utf-8') as file:
    for i in range(25):
        data = file.write(f'{randrange(111, 778)} \n')

# Случайные числа
# Напишите программу, записывающую в текстовый файл random.txt 2525 случайных чисел в диапазоне от 111111 до 777777 (включительно), каждое с новой строки.
#
# Формат входных данных
# На вход программе ничего не подается.
#
# Формат выходных данных
# Программа должна создать файл с именем random.txt и записать в него случайные числа в соответствии с условием задачи.
#
# Примечание 1. Считайте, что исполняемая программа и указанный файл находятся в одной папке.
#
# Примечание 2. Для генерации случайных чисел используйте модуль random.
