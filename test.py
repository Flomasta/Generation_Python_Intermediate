# put your python code here
from functools import reduce


def evaluate(coefficients, x):
    coef = map(lambda c, ex, d: str((int(c)) * ex ** d), coefficients.split()[::-1], [int(x)] * len(coefficients),
               range(0, len(coefficients)))
    coef = reduce(lambda x, y: x + int(y), coef, 0)
    return coef


print(evaluate(input(),input()))
