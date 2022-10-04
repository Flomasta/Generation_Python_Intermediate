n, m = int(input()), int(input())
max = -1000
for i in range(n):
    row = list(map(int, input().split()))
    for j in row:
        if j > max:
            max = j
            c = i
            b = row.index(j)

print(c, b)
