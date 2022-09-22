n = int(input())
lst = []

for i in range(0, n):
    row = [1] * (i + 1)
    for j in range(i):
        if j != 0 and j != i:
            row[j] = sum(lst[i - 1][j - 1:j + 1])
    lst.append(row)
    print(*row)
