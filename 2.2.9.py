amount = int(input())
fridges = [input() for i in range(amount)]
mask = 'anton'
fridges_nums = []

for fridge in fridges:
    letter = 0
    res = ''
    for i in mask:
        for j in range(letter, len(fridge)):
            if fridge[j] == i:
                letter = j + 1
                res += fridge[j]
                break
    if res == mask:
        fridges_nums.append(fridges.index(fridge) + 1)
print(*fridges_nums)
