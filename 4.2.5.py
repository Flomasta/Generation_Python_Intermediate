data = input().split()
lst = []

for i in data:
    if lst and i in lst[-1]:
        lst[-1].append(i)
    else:
        lst.append([i])
print(lst)

# w w w o r l d g g g g r e a t t e c c h e m g g p w w
