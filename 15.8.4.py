is_non_negative_num = lambda x: True if x.replace('.', '', 1).isdigit() and '-' not in x[1:] and x[0] != '.' else False



# отлично
# is_num = lambda x: x.replace('-', '', x[0] == '-').replace('.', '', 1).isdigit()

# Напишите функцию is_num, используя синтаксис анонимных функций, которая принимает строковый аргумент и возвращает значение True, если переданный аргумент является числом (целым или вещественным) и False в противном случае.
#
# Примечание 1. Следующий программный код:
#
# print(is_num('10.34ab'))
# print(is_num('10.45'))
# print(is_num('-18'))
# print(is_num('-34.67'))
# print(is_num('987'))
# print(is_num('abcd'))
# print(is_num('123.122.12'))
# print(is_num('-123.122'))
# print(is_num('--13.2'))
# должен выводить:
#
# False
# True
# True
# True
# True
# False
# False
# True
# False
# Примечание 2. Используйте вспомогательную функцию из прошлого степа.
#
# Примечание 3. Вызывать анонимную функцию не нужно.
