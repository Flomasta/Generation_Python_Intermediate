letters = input().split()

for i in range(len(letters)):
    counter = letters[:i].count(letters[i])
    if counter:
        print(f'{letters[i]}_{counter}', end=' ')
    else:
        print(letters[i], end=' ')
