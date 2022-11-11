print(*map(lambda x: 255-int(x),input().split()))


# Противоположный цвет
# В цветовой схеме RGB цвета задаются с помощью трех компонентов:
#
# R — интенсивность красной составляющей цвета;
# G — интенсивность зеленой составляющей цвета;
# B — интенсивность синей составляющей цвета.
# Противоположные цвета задаются как RGB и (255-R)(255-G)(255-B). Считается, что такие цвета хорошо гармонируют друг с другом.
#
# Напишите программу, которая по трем компонентам заданного цвета, находит компоненты противоположного цвета.
#
# Формат входных данных
# На вход программе подается строка, содержащая три целых неотрицательных числа, компоненты R, G и B начального цвета,  разделенные символом пробела.
#
# Формат выходных данных
# Программа должна вывести три компонента R, G и B противоположного цвета, разделенные символом пробела.
#
# Примечание. Попробуйте решить задачу в одну строку с помощью встроенной функции map().
