n, m = map(int, input().split())
mtx = [[0] * m for i in range(n)]

counter = 1
x, y = 0, -1
d_row = 0
d_col = 1
while counter <= n * m:
    if 0 <= x + d_row < n and 0 <= y + d_col < m and mtx[x + d_row][y + d_col] == 0:
        x += d_row
        y += d_col
        mtx[x][y] = counter
        counter += 1
    else:
        if d_col == 1:
            d_col = 0
            d_row = 1
        elif d_row == 1:
            d_row = 0
            d_col = -1
        elif d_col == -1:
            d_col = 0
            d_row = -1
        elif d_row == -1:
            d_row = 0
            d_col = 1
[print(*i) for i in mtx]
