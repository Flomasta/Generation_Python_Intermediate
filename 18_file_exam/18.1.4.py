with open('../txt_files_for_part_files_and_files_exam/words.txt', 'r', encoding='utf-8') as file:
    data = file.read().split()
    l = len(sorted(data, key=len)[-1])
    print(*filter(lambda x: len(x) == l, data), sep='\n')

# Самое длинное слово в файле
# Вам доступен текстовый файл words.txt со словами, разделенными пробелом. Напишите программу, которая находит и выводит самые длинные слова этого файла, не меняя порядка их следования.
#
# Формат входных данных
# На вход программе ничего не подается.
#
# Формат выходных данных
# Программа должна вывести самые длинные слова файла words.txt, каждое с новой строки, не меняя их порядка следования.
#
# Примечание 1. Считайте, что исполняемая программа и указанный файл находятся в одной папке.
#
# Примечание 2. Словом считайте любую группу символов без пробелов, даже если она включает цифры или знаки препинания.
#
# Примечание 3. Если бы файл words.txt содержал строки:
#
# there are many different holidays on the first of january we celebrate new year on the seventh of january and the twenty-fifth of december we have christmas the twenty-third of february is the day of the defenders of the motherland or the army day then comes easter and radonitsa the first of may is the labour day the ninth of may is victory day the third of july is independence day then comes the seventh of november the day of the october revolution and so on
# то результатом будет:
#
# twenty-fifth
# twenty-third
# independence
# Примечание 4. Указанный файл можно скачать по ссылке.
