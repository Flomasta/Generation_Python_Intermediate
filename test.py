n, m = set(input()), set(input())
mask = {*range(10)}
res = {*set(map(int,n)), *set(map(int,m))}
print('YES' if mask == res else 'NO')

# Наполните множество set1 содержимым так, чтобы программа вывела {'p'}.
