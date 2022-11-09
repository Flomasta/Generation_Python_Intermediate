def mean(*args):
    res = [i for i in list(args) if type(i) == int or type(i) == float]
    if len(res) > 0:
        return sum(res) / len(res)
    else:
        return len(res)


print(mean(1.5, True, ['stepik'], 'beegeek', 2.5))
