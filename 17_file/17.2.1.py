with open('../text.txt', encoding='utf-8') as file:
    print(file.readline().strip()[::-1])

# Переворот строки
# Вам доступен текстовый файл text.txt с одной строкой текста. Напишите программу, которая выводит на экран эту строку в обратном порядке.
#
# Формат входных данных
# На вход программе ничего не подается.
#
# Формат выходных данных
# Программа должна вывести строку указанного файла в обратном порядке.
#
# Примечание 1. Считайте, что исполняемая программа и указанный файл находятся в одной папке.
#
# Примечание 2. Используйте менеджер контекста 🙂.
#
# Примечание 3. Указанный файл можно скачать по ссылке.