string = str(round((len(input()) * 0.6), 2)).split('.')
print(string[0] + ' р. ' + str(int(string[1]) * 10) + ' коп.')
