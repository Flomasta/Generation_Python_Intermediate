n = int(input())
row = []
for i in range(1, n + 1):
    row.append(list(range(1, i + 1)))
print(*row, sep='\n')
