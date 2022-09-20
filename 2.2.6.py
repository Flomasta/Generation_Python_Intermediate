n = int(input())
lst = [int(input()) for i in range(n)]
n_to_check = int(input())
flag = False


def check_sum(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            yield lst[i] * lst[j]


for i in check_sum(lst):
    if i == n_to_check:
        flag = True
        break

print('ДА' if flag else 'НЕТ')
