d = {'A': 'U', 'C': 'G', 'G': 'C', 'T': 'A'}

print(*[d[i] for i in list(input())], sep='')


# Минутка генетики
# Как известно из курса биологии ДНК и РНК – последовательности нуклеотидов.
#
# Четыре нуклеотида в ДНК:
#
# аденин (A);
# цитозин (C);
# гуанин (G);
# тимин (T).
# Четыре нуклеотида в РНК:
#
# аденин (A);
# цитозин (C);
# гуанин (G);
# урацил (U).
# Цепь РНК строится на основе цепи ДНК последовательным присоединением комплементарных нуклеотидов:
#
# G \rightarrow→ C;
# C \rightarrow→ G;
# T \rightarrow→ A;
# A \rightarrow→ U.
# Напишите программу, переводящую цепь ДНК в цепь РНК.
#
# Формат входных данных
# На вход программе подается корректная цепь ДНК в верхнем регистре.
#
# Формат выходных данных
# Программа должна вывести соответствующую цепь РНК в верхнем регистре.
#
# Примечание. Подробнее прочитать про ДНК и РНК можно тут и тут.
#
# Тестовые данные 🟢
# Sample Input 1:
#
# ACTG
# Sample Output 1:
#
# UGAC
# Sample Input 2:
#
# CC
# Sample Output 2:
#
# GG
# Sample Input 3:
#
# GTA
# Sample Output 3:
#
# CAU