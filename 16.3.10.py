def gematria(data):
    return sum(list(map(lambda x: ord(x) - ord('A'), data.upper())))


data = sorted([input() for i in range(int(input()))])
for i in data:
    print(gematria(i))

print(*list(sorted(data, key=gematria)), sep='\n')

# Гематрия слова
# Гематрией слова называется сумма числовых значений входящих в него букв.
#
# Для вычисления гематрии слова в этой задаче:
#
# переведём слово в верхний регистр;
# числовое значение буквы вычислим как код(буквы) - код(буквы A).
# На вход программе подается натуральное число nn, а затем nn строк английских слов в разных регистрах.
#
# Напишите программу, которая выводит слова в начальном регистре (каждое на отдельной строке) в порядке возрастания их гематрии. Если гематрия слов совпадает, они выводятся в алфавитном (лексикографическом) порядке.
#
# Формат входных данных
# На вход программе подается натуральное число nn, а затем nn строк английских слов в разных регистрах.
#
# Формат выходных данных
# Программа должна отсортировать слова в соответствии с условием задачи.
#
# Примечание 1. Для получения кода символа воспользуйтесь встроенной функцией ord().
#
# Примечание 2. Слова во входных данных могут повторяться.
#
# Примечание 3. Пусть требуется вычислить гематрию слова BaSis. Переводим его в верхний регистр BASIS. Для каждого символа в слове находим его код с помощью встроенной функции ord():
#
# ord('B') = 66
# ord('A') = 65
# ord('S') = 83
# ord('I') = 73
# ord('S') = 83
# В соответствии с условием задачи вычисляем числовое значение буквы как код(буквы) - код(буквы A). Вычитаем из кода каждой буквы значение ord('A') = 65:
#
# ord('B') - ord('A') = 66 - 65 = 1
# ord('A') - ord('A') = 65 - 65 = 0
# ord('S') - ord('A') = 83 - 65 = 18
# ord('I') - ord('A') = 73 - 65 = 8
# ord('S') - ord('A') = 83 - 65 = 18
# Гематрия слова BaSis равна 1+0+18+8+18 = 451+0+18+8+18=45.