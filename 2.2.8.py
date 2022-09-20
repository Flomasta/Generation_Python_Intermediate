timur, ruslan = input(), input()
win_combinations = ['ножницыбумага', 'бумагакамень', 'каменьящерица', 'ящерицаСпок', 'Спокножницы', 'ножницыящерица',
                    'ящерицабумага', 'бумагаСпок', 'Споккамень', 'каменьножницы']
if timur == ruslan:
    print('ничья')
elif timur + ruslan in win_combinations:
    print('Тимур')
else:
    print('Руслан')
