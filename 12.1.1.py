import random

lst = ['Орел', 'Решка']
n = int(input())  # количество попыток
for i in range(n):
    print(lst[random.randrange(0, 2)])
    
# Напишите программу, которая с помощью модуля random моделирует броски монеты. Программа принимает на вход количество попыток и выводит результаты бросков: Орел или Решка (каждое на отдельной строке).
#
# Примечание. Например, при n=7n=7 ваша программа может выводить:
#
# Орел
# Решка
# Решка
# Орел
# Орел
# Орел
# Решка
# Для отладки кода 🟡
