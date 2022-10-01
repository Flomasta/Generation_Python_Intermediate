n = int(input())
matrix = [list(map(int, input().split())) for i in range(n)]
lst = [[], [], [], []]
for i in range(n):
    for j in range(n):
        a = matrix[i][j]
        if i < j and i < n - 1 - j:
            lst[0].append(matrix[i][j])
        elif i < j and i > n - 1 - j:
            lst[1].append(matrix[i][j])
        elif i > j and i > n - 1 - j:
            lst[2].append(matrix[i][j])
        elif i > j and i < n - 1 - j:
            lst[3].append(matrix[i][j])
        b = lst
quaters = ['Верхняя четверть: ', 'Правая четверть: ', 'Нижняя четверть: ', 'Левая четверть: ']

[print(quaters[i], sum(lst[i]), sep='') for i in range(len(lst))]
