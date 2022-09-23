data = input().split()
lst = [[]]
ld = len(data)
for i in range(ld):
    for j in range(0, ld - i):
        lst.append(data[j: i + 1 + j])
print(lst)


#a b v
