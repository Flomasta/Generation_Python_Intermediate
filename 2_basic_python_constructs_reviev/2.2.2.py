lst = list(map(int, input().split()))
print(sum([1 for i in range(1,len(lst)) if lst[i - 1] < lst[i]]))
