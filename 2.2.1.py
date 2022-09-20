amount = int(input())

lst = [map(int, input().split()) for i in range(amount)]
one, two, three, four = 0, 0, 0, 0
for i in lst:
    x, y = i
    if x > 0 and y > 0:
        one += 1
    elif x < 0 and y > 0:
        two += 1
    elif x < 0 and y < 0:
        three += 1
    elif x > 0 and y < 0:
        four += 1

print(f'''Первая четверть: {one}
Вторая четверть: {two}
Третья четверть: {three}
Четвертая четверть: {four}''')
