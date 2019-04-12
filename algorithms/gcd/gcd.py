import math


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


a = 3 * 3 * 5 * 5 * 13
b = 2 * 3 * 5 * 7 * 11
assert(math.gcd(a, b) == gcd(a, b))
