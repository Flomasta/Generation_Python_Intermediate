with open('class_scores.txt', 'r', encoding='utf-8') as data_file, open('new_scores', 'a', encoding='utf-8') as file:
    data = data_file.readlines()
    data = map(
        lambda x: f'{x.split()[0]} 100' if int(
            x.split()[1]) + 5 > 100 else f'{x.split()[0]} {str(int(x.split()[1]) + 5)}',
        data)
    print(*data, file=file, sep='\n')

    # Подарок на новый год
    # Вам доступен текстовый файл class_scores.txt с оценками за итоговый тест на строках вида: фамилия оценка (фамилия и оценка разделены пробелом). Оценка - целое число от 00 до 100100 включительно.
    #
    # Напишите программу для добавления 55 баллов к каждому результату теста и вывода фамилий и новых результатов тестов в файл new_scores.txt.
    #
    # Формат входных данных
    # На вход программе ничего не подается.
    #
    # Формат выходных данных
    # Программа должна создать файл с именем new_scores.txt в соответствии с условием задачи.
    #
    # Примечание 1. Считайте, что исполняемая программа и указанные файлы находятся в одной папке.
    #
    # Примечание 2. Если бы файл class_scores.txt содержал строки:
    #
    # Washington 83
    # Adams 86
    # Kingsman 100
    # MacDonald 95
    # Thomson 98
    # то файл new_scores.txt имел бы вид:
    #
    # Washington 88
    # Adams 91
    # Kingsman 100
    # MacDonald 100
    # Thomson 100
