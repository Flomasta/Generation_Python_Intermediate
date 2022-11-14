with open('../txt_files_for_part_files_and_files_exam/goats.txt', 'r', encoding='utf-8') as data_file, open(
        '../txt_files_for_part_files_and_files_exam/answer_goats.txt', 'a', encoding='utf-8') as file:
    data = list(map(lambda x: x.split()[0], data_file.readlines()))
    s_data = set(data[0:data.index('GOATS')])
    nums = {}
    for i in s_data:
        nums.update({i: list(data).count(f'{i}') - 1})
    [nums.pop(i, None) for i in ['COLOURS', 'GOATS']]
    percent = int(sum(nums.values()) / 100 * 7)
    items = list(filter(lambda x: x[1] > percent, nums.items()))
    print(*sorted([f'{i[0]} goat' for i in items]), file=file, sep='\n')

    # s_data.remove('COLOURS')
    # s_data.remove('GOATS')
    # print(*[f'{item} goat' for item in sorted(s_data)], file=file, sep='\n')

# Загадка от Жака Фреско 🌶️
# Однажды Жака Фреско спросили:
#
# "Если ты такой умный, почему не богатый?"
#
# Жак не стал отвечать на столь провокационный вопрос, вместо этого он задал загадку спрашивающему:
#
# "Были разноцветные козлы. Сколько?"
#
# "Сколько чего?"
#
# "Сколько из них составляет более 7% от общего количества козлов?"
#
# Вам доступен текстовый файл goats.txt в первой строке которого написано слово COLOURS, далее идет список всех возможных цветов козлов. Затем идет строка со словом GOATS, и далее непосредственно перечисление козлов разных цветов. Перечень козлов включает только строки из первого списка.
#
# Напишите программу создания файла answer.txt и вывода в него списка козлов, которые удовлетворяют условию загадки от Жака Фреско.
#
# Формат входных данных
# На вход программе ничего не подается.
#
# Формат выходных данных
# Программа должна создать файл с именем answer.txt и вывести в него в алфавитном порядке названия цветов козлов, которые удовлетворяют условию загадки Жака Фреско.
#
# Примечание 1. Считайте, что исполняемая программа и указанные файлы находятся в одной папке.
#
# Примечание 2. Если бы файл goats.txt содержал строки:
#
# COLOURS
# Pink goat
# Green goat
# Black goat
# GOATS
# Pink goat
# Pink goat
# Black goat
# Pink goat
# Pink goat
# Black goat
# Green goat
# Pink goat
# Black goat
# Black goat
# Pink goat
# Pink goat
# Black goat
# Black goat
# Pink goat
# то файл answer.txt имел бы вид:
#
# Black goat
# Pink goat
# Примечание 3. Указанный файл можно скачать по ссылке.
