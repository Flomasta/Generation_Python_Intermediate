timur, ruslan = input().lower(), input().lower()
win_combinations = ['ножницыбумага', 'бумагакамень', 'каменьящерица', 'ящерицаспок', 'спокножницы', 'ножницыящерица',
                    'ящерицабумага', 'бумагаспок', 'споккамень', 'каменьножницы']
if timur == ruslan:
    print('ничья')
elif timur + ruslan in win_combinations:
    print('Тимур')
else:
    print('Руслан')
