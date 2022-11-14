lst = list(map(int, input().split()))
print(*[lst[-1]] + lst[0:-1:1])
