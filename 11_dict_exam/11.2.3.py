d = {'A': 1, 'E': 1, 'I': 1, 'L': 1, 'N': 1, 'O': 1, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'D': 2, 'G': 2, 'B': 3, 'C': 3,
     'M': 3, 'P': 3, 'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4, 'K': 5, 'J': 8, 'X': 8, 'Q': 10, 'Z': 10}

txt = list(input().upper())
print(sum([d[i] for i in txt]))

# Scrabble game
# В игре Scrabble каждая буква приносит определенное количество баллов. Общая стоимость слова – сумма баллов его букв. Чем реже буква встречается, тем больше она ценится:
#
# Баллы	Буква
# 11	AA, EE, II, LL, NN, OO, RR, SS, TT, UU
# 22	DD, GG
# 33	BB, CC, MM, PP
# 44	FF, HH, VV, WW, YY
# 55	KK
# 88	JJ, XX
# 1010	QQ, ZZ
# Напишите программу подсчета итоговой стоимости введенного слова.
#
# Формат входных данных
# На вход программе подается одно слово в верхнем регистре на английском языке.
#
# Формат выходных данных
# Программа должна вывести суммарную стоимость букв введеного слова.
#
# Примечание. Подробнее про игру можно почитать тут.