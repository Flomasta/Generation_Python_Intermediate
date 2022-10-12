n = input().lower()
m = 8
d = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
chessmate = [['.' for i in range(m)] for j in range(m)]

x, y = m - int(n[1]), d[n[0]]
chessmate[x][y] = 'N'
for i in range(m):
    for j in range(m):
        if abs(x - i) == 1 and abs(y - j) == 2 or abs(x - i) == 2 and abs(y - j) == 1:
            chessmate[i][j] = '*'
[print(*i) for i in chessmate]

# вариант решения:
# x, y = list(input())
# x, y = 'abcdefgh'.index(x), 8 - int(y)
# arr = [['.*'[abs((x - j) * (y - i)) == 2] for j in range(8)] for i in range(8)]
# arr[y][x] = 'N'
# [print(*row) for row in arr]
