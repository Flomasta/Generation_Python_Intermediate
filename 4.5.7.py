n = int(input())
matrix = [list(map(int, input().split())) for i in range(n)]
matrix.reverse()
[print(*i) for i in zip(*matrix)]
