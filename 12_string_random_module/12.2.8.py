from string import *
from random import sample


def generate_password(length):
    LETTER = list(''.join((set(ascii_letters) | set(digits)) - set('lI1oO0')))
    return ''.join(sample(LETTER, length))


def generate_passwords(count, length):
    for i in range(count):
        print(generate_password(length))


n, m = int(input()), int(input())
generate_passwords(n, m)
