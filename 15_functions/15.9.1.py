def ignore_command(command):
    ignore = ['alias', 'configuration', 'ip', 'sql', 'select', 'update', 'exec', 'del', 'truncate']

    return  any( [word in command for word in ignore])


print(ignore_command('get ip'))
print(ignore_command('select all'))
print(ignore_command('delete'))
print(ignore_command('trancate'))
# Тестовые данные 🟢
# Sample Input 1:
#
# 2 4 3
# 10
# Sample Output 1:
#
# 243
# Sample Input 2:
#
# 1 2 3 4 5 6 7
# 1
# Sample Output 2:
#
# 28
# Sample Input 3:
#
# -2 4 5
# 3
# Sample Output 3:
#
# -1
# Sample Input 4:
#
# 10
# 2
# Sample Output 4:
#
# 10
# Sample Input 5:
#
# 3 19
# 10
# Sample Output 5:
#
# 49
