from random import sample


def generate_ip():
    ip_lst = sample(list(map(str, range(1, 256))), 4)
    return '.'.join(ip_lst)


print(generate_ip())


#Вариант
# from random import randrange as r
#
# def generate_ip():
#     return f'{r(256)}.{r(256)}.{r(256)}.{r(256)}'



# IP адрес состоит из четырех чисел из диапазона от 00 до 255255 (включительно) разделенных точкой.
#
# Напишите функцию generate_ip(), которая с помощью модуля random  генерирует и возвращает случайный корректный IP адрес.
#
# Примечание 1. Пример правильного (неправильного) IP адреса:
#
# 192.168.5.250        # правильный
# 199.300.521.255      # неправильный
# Примечание 2. Вызывать функцию generate_ip() не нужно, требуется только реализовать.
