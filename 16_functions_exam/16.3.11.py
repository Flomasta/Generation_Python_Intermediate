def checker(data):
    data = map(int, data.split('.'))
    data = map(lambda num, degree: num * 256 ** degree, data, range(3, -1, -1))
    return sum(list(data))


data = [input() for _ in range(int(input()))]

print(*sorted(data, key=checker),sep='\n')


# Сортировка IP-адресов
# IP-адрес – уникальный числовой идентификатор устройства в компьютерной сети, работающий по протоколу TCP/IP.
#
# В 44-й версии IP-адрес представляет собой 3232-битное число. Адрес записывается в виде четырёх десятичных чисел (октетов) со значением от 00 до 255255, разделённых точками, например, 192.168.1.2192.168.1.2.
#
# Напишите программу, которая считывает IP-адреса и выводит их в порядке возрастания в соответствии с десятичным представлением.
#
# Формат входных данных
# На вход программе подается число n \, (n \ge 1)n (n≥1) – количество IP-адресов. Затем nn строк с корректными IP-адресами.
#
# Формат выходных данных
# Программа должна вывести IP-адреса в порядке возрастания в соответствии с десятичным представлением.
#
# Примечание 1. Чтобы перевести IP-адрес 192.168.1.2 в десятичное число мы используем формулу:
#
# 192 \cdot 256^3 + 168 \cdot 256^2 + 1 \cdot 256^1 + 2 \cdot 256^0 = 3232235778
# 192⋅256
# 3
# +168⋅256
# 2
# +1⋅256
# 1
# +2⋅256
# 0
# =3232235778
# Примечание 2. Используйте необязательный аргумент key.