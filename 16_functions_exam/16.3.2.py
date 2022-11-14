from functools import reduce


def checker(data):
    return data % 2 == 1


def reducer(x, y):
    return x * y


def product_of_odds(data):
    return reduce(reducer, filter(checker, data), 1)


print(product_of_odds([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
