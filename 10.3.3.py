text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'

result = {}
for letter in text:
    result[letter] = result.get(letter, 0) + 1
print(result)

#хорошее решение
#
# text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'
#
# result = {elem: text.count(elem) for elem in set(text)}

# Дополните приведенный код так, чтобы в переменной result хранился словарь, в котором для каждого символа строки text будет подсчитано количество его вхождений.
#
# Примечание. Выводить содержимое словаря result не нужно.
