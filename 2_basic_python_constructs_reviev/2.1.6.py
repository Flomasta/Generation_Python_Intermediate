num = input()
print(num[0] + num[-1:0:-1] if len(num) > 5 else int(num[::-1]))
