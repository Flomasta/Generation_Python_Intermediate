n = int(input())
lst = []
s = 0
for i in range(n):
    lst.append([*map(int, input().split())])
    s += lst[i][i]
print(s)
