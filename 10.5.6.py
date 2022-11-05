numbers = [34, 10, 4, 6, 10, 23, 90, 100, 21, 35, 95, 1, 36, 38, 19, 1, 6, 87, 1000, 13456, 360]

result = sorted({i: [j for j in range(1, i + 1) if i % j == 0] for i in numbers}.items())

print(dict(result))

# оптимизированный результат, сокращение каждого цикла в 2 раза
# добавляем n т.к в условии сказано, что все делители должны быть в списке

# result = {n: [i for i in range(1, n // 2 + 1) if n % i == 0] + [n] for n in numbers}


# Используя генератор, дополните приведенный код, чтобы получить словарь result , где ключом будет элемент списка numbers, а значением – отсортированный по возрастанию список всех его делителей начиная с 11.
#
# Примечание 1. Если бы список numbers имел вид: numbers = [1, 6, 18], то результатом был бы словарь
#
# result = {1: [1], 6: [1, 2, 3, 6], 18: [1, 2, 3, 6, 9, 18]}
# Примечание 2. Выводить содержимое словаря result не нужно.
