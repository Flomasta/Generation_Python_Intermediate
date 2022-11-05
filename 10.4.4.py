n = int(input())
d = {}
for _ in range(n):
    k, v = input().split()
    d[k] = v
word = input()
for i in d.items():
    if word in i:
        print(*set(i).difference(set((word,))))
        break
# Beautiful Pretty

# Словарь синонимов
# Вам дан словарь, состоящий из пар слов-синонимов. Повторяющихся слов в словаре нет. Напишите программу, которая для одного данного слова определяет его синоним.
#
# Формат входных данных
# На вход программе подается количество пар синонимов nn. Далее следует nn строк, каждая строка содержит два слова-синонима. После этого следует одно слово, синоним которого надо найти.
#
# Формат выходных данных
# Программа должна вывести одно слово, синоним введенного.
#
# Примечание 1. Гарантируется, что синоним введенного слова существует в словаре.
#
# Примечание 2. Все слова в словаре начинаются с заглавной буквы.
#
# Тестовые данные 🟢
# Sample Input 1:
#
# 4
# Awful Terrible
# Beautiful Pretty
# Great Excellent
# Generous Bountiful
# Pretty
# Sample Output 1:
#
# Beautiful
# Sample Input 2:
#
# 3
# Kind Affable
# Intellect Mind
# Popular Celebrated
# Popular
# Sample Output 2:
#
# Celebrated
