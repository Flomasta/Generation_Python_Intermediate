a, b, = input().lower().split(), input().lower().split()
d1, d2 = {}, {}

for i in a:
    for j in i.strip('.,!?:;-'):
        d1[j] = d1.get(j, 0) + 1
for i in b:
    for j in i.strip('.,!?:;-'):
        d2[j] = d2.get(j, 0) + 1

print(['NO', 'YES'][d2 == d1])


# Анаграммы 2
# На вход программе подаются два предложения. Напишите программу, которая определяет, являются они анаграммами или нет. Ваша программа должна игнорировать регистр символов, знаки препинания и пробелы.
#
# Формат входных данных
# На вход программе подаются два предложения, каждое на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести YES , если предложения – анаграммы и NO в противном случае.
#
# Примечание. Кроме слов в тексте могут присутствовать пробелы и знаки препинания .,!?:;-. Других символов в тексте нет.
#
# Тестовые данные 🟢
# Sample Input 1:
#
# Вижу зверей
# Живу резвей
# Sample Output 1:
#
# YES
# Sample Input 2:
#
# Когда увидимся
# тогда и свидимся
# Sample Output 2:
#
# NO
# Sample Input 3:
#
# С мая весной
# сам я не свой
# Sample Output 3:
#
# YES
