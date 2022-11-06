import string
from random import sample, choice


def generate_index():
    alph = list(string.ascii_uppercase)
    nums = list(range(0, 100))
    idx = ''.join(sample(alph, 2)) + str(choice(nums)) + '_' + str(choice(nums)) + ''.join(sample(alph, 2))
    return idx


print(generate_index())

#вариант
# from random import choice, randint
# from string import ascii_uppercase as letter
#
# def generate_index():
#     return f'{choice(letter)}{choice(letter)}{randint(0, 99)}_{randint(0, 99)}{choice(letter)}{choice(letter)}'



# Почтовый индекс в Латверии имеет вид: LetterLetterNumber_NumberLetterLetter, где Letter – заглавная буква английского алфавита, Number – число от 00 до 9999 (включительно).
#
# Напишите функцию generate_index(), которая с помощью модуля random генерирует и возвращает случайный корректный почтовый индекс Латверии.
#
# Примечание 1. Пример правильного (неправильного) индекса Латверии:
#
# AB23_56VG          # правильный
# V3F_231GT          # неправильный
# Примечание 2. Обратите внимание на символ _ в почтовом индексе.
#
# Примечание 3. Вызывать функцию generate_index() не нужно, требуется только реализовать.
#
