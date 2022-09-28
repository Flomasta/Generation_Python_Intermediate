rows, cols = int(input()), int(input())

lst = []

for r in range(rows):
    row = []
    for c in range(cols):
        row.append(input())
    lst.append(row)

for r in range(rows):
    for c in range(cols):
        print(lst[r][c], end=' ')
    print()

for c in range(cols):
    for r in range(rows):
        print(lst[r][c], end=' ')
    print()
