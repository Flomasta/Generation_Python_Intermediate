n = int(input())
lst = []
for i in range(0, n + 1):
    row = [1] * (i + 1)
    for j in range(i + 1):
        if j != i and j != 0:
            row[j] = lst[i - 1][j - 1] + lst[i - 1][j]
    lst.append(row)
print(lst[n])
