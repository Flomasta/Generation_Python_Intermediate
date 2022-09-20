timur, ruslan = input(), input()
lst = ['камень', 'ножницы', 'бумага']
idx_t = lst.index(timur)
idx_r = lst.index(ruslan)

if idx_t - idx_r == -1 or idx_t - idx_r == 2:
    print('Тимур')
elif timur == ruslan:
    print('ничья')
else:
    print('Руслан')
